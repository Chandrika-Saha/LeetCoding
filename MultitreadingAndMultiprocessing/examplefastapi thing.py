from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import boto3, uuid, time, json, os

# ------------------
# Config (env vars with defaults)
# ------------------
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "")          # required in prod
JOB_TABLE = os.getenv("JOB_TABLE", "jobs")              # DynamoDB table name
RESULT_BUCKET = os.getenv("RESULT_BUCKET", "")          # required in prod
RESULT_PREFIX = os.getenv("RESULT_PREFIX", "results")   # S3 folder/prefix
PRESIGN_SECONDS = int(os.getenv("PRESIGN_SECONDS", "900"))


if not SQS_QUEUE_URL:
    raise RuntimeError("Missing env var: SQS_QUEUE_URL")
if not RESULT_BUCKET:
    raise RuntimeError("Missing env var: RESULT_BUCKET")

# ------------------
# AWS clients
# ------------------
sqs = boto3.client("sqs", region_name=AWS_REGION)
ddb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = ddb.Table(JOB_TABLE)
s3 = boto3.client("s3", region_name=AWS_REGION)

app = FastAPI()

# ------------------
# Models (store products)
# ------------------
class ProductItem(BaseModel):
    product_id: str = Field(..., min_length=1, max_length=64)
    name: str = Field(..., min_length=1, max_length=200)
    quantity: int = Field(..., ge=1, le=100)
    unit_price: float = Field(..., ge=0.0, le=100000.0)

class OrderRequest(BaseModel):
    customer_id: str = Field(..., min_length=1, max_length=64)
    items: List[ProductItem] = Field(..., min_length=1, max_length=50)
    currency: str = Field(default="USD", min_length=3, max_length=3)

class JobResponse(BaseModel):
    job_id: str
    status: str
    result_url: Optional[str] = None

# ------------------
# Routes
# ------------------
@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/orders", response_model=JobResponse)
def submit_order(req: OrderRequest):
    job_id = str(uuid.uuid4())
    now = int(time.time())

    # 1) Store job state (DynamoDB)
    table.put_item(Item={
        "job_id": job_id,
        "status": "queued",
        "created_at": now
    })

    # 2) Send job to SQS (worker will process the order)
    sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=json.dumps({
            "job_id": job_id,
            "payload": req.model_dump()
        })
    )

    return {"job_id": job_id, "status": "queued"}

@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: str):
    resp = table.get_item(Key={"job_id": job_id})
    if "Item" not in resp:
        raise HTTPException(404, "Job not found")

    job = resp["Item"]

    # If finished, return presigned S3 URL for result JSON
    result_url = None
    if job.get("status") == "done":
        result_url = s3.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": RESULT_BUCKET,
                "Key": f"{RESULT_PREFIX}/{job_id}.json"
            },
            ExpiresIn=PRESIGN_SECONDS
        )

    return {
        "job_id": job_id,
        "status": job.get("status", "unknown"),
        "result_url": result_url
    }
