# worker_gpu.py
import os, json, time, traceback
from typing import Any, Dict, List

import boto3
import torch

# ------------------
# Config (env vars)
# ------------------
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "")
JOB_TABLE = os.getenv("JOB_TABLE", "jobs")
RESULT_BUCKET = os.getenv("RESULT_BUCKET", "")
RESULT_PREFIX = os.getenv("RESULT_PREFIX", "results")

POLL_WAIT_SECONDS = int(os.getenv("POLL_WAIT_SECONDS", "20"))        # long polling
MAX_MESSAGES = int(os.getenv("MAX_MESSAGES", "1"))                   # start with 1 per worker
VISIBILITY_TIMEOUT = int(os.getenv("VISIBILITY_TIMEOUT", "300"))     # must be > max inference time

if not SQS_QUEUE_URL:
    raise RuntimeError("Missing SQS_QUEUE_URL")
if not RESULT_BUCKET:
    raise RuntimeError("Missing RESULT_BUCKET")

# ------------------
# AWS clients
# ------------------
sqs = boto3.client("sqs", region_name=AWS_REGION)
ddb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = ddb.Table(JOB_TABLE)
s3 = boto3.client("s3", region_name=AWS_REGION)

# ------------------
# Minimal "model"
# Replace with your real load + inference
# ------------------
class Model:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # load weights here, move to GPU, etc.

    @torch.no_grad()
    def infer(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        payload is whatever your API sent in SQS:
        { customer_id, items:[{product_id,name,quantity,unit_price}], currency }
        """
        # Example: compute order total
        total = 0.0
        for item in payload["items"]:
            total += float(item["unit_price"]) * int(item["quantity"])

        return {
            "currency": payload.get("currency", "USD"),
            "total": round(total, 2),
            "num_items": len(payload["items"]),
        }

model = Model()

# ------------------
# DynamoDB helpers
# ------------------
def set_status(job_id: str, status: str, **extra):
    now = int(time.time())

    # Build a dynamic update expression
    expr_parts = ["#s = :s", "updated_at = :u"]
    names = {"#s": "status"}
    values = {":s": status, ":u": now}

    for k, v in extra.items():
        expr_parts.append(f"{k} = :{k}")
        values[f":{k}"] = v

    table.update_item(
        Key={"job_id": job_id},
        UpdateExpression="SET " + ", ".join(expr_parts),
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
    )

def write_result(job_id: str, result: Dict[str, Any]) -> str:
    key = f"{RESULT_PREFIX}/{job_id}.json"
    s3.put_object(
        Bucket=RESULT_BUCKET,
        Key=key,
        Body=json.dumps(result).encode("utf-8"),
        ContentType="application/json",
    )
    return f"s3://{RESULT_BUCKET}/{key}"

# ------------------
# Main worker loop
# ------------------
def run():
    print("GPU worker started.")
    print("CUDA available:", torch.cuda.is_available())

    while True:
        resp = sqs.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            MaxNumberOfMessages=MAX_MESSAGES,
            WaitTimeSeconds=POLL_WAIT_SECONDS,
            VisibilityTimeout=VISIBILITY_TIMEOUT,
        )

        messages = resp.get("Messages", [])
        if not messages:
            continue

        for msg in messages:
            receipt = msg["ReceiptHandle"]

            try:
                body = json.loads(msg["Body"])
                job_id = body["job_id"]
                payload = body["payload"]  # sent from API

                # Mark running
                set_status(job_id, "running")

                # Do inference
                start = time.time()
                output = model.infer(payload)
                runtime_ms = (time.time() - start) * 1000.0

                # Build and save result
                result_doc = {
                    "job_id": job_id,
                    "status": "done",
                    "runtime_ms": runtime_ms,
                    "output": output,
                }
                s3_uri = write_result(job_id, result_doc)

                # Mark done + store S3 location
                set_status(job_id, "done", result_s3_uri=s3_uri)

                # Only now delete message
                sqs.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=receipt)
                print(f"[OK] {job_id} -> {s3_uri}")

            except Exception as e:
                # Best-effort mark failed (don’t crash the worker)
                err = f"{type(e).__name__}: {e}"
                tb = traceback.format_exc(limit=3)
                print(f"[ERR] {err}\n{tb}")

                # If we can extract job_id, mark failed
                try:
                    body = json.loads(msg["Body"])
                    job_id = body.get("job_id")
                    if job_id:
                        set_status(job_id, "failed", error=err)
                except Exception:
                    pass

                # Decide retry strategy:
                # For now, delete to avoid infinite retries.
                # In production: send to DLQ after maxReceiveCount.
                sqs.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=receipt)

if __name__ == "__main__":
    run()
