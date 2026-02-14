# app.py
from flask import Flask, request, jsonify
import torch, uuid, time
from dataclasses import dataclass, asdict
from typing import List

app = Flask(__name__)

# ---- simple validation helpers (Flask doesn't validate like FastAPI) ----
def in_range(name, v, lo, hi):
    if not isinstance(v, (int, float)) or v < lo or v > hi:
        raise ValueError(f"{name} must be in [{lo}, {hi}]")

@dataclass
class VehicleState:
    x: float
    y: float
    velocity: float
    heading: float

def parse_vehicle(d) -> VehicleState:
    x, y, vel, head = d["x"], d["y"], d["velocity"], d["heading"]
    in_range("x", x, -1000, 1000)
    in_range("y", y, -1000, 1000)
    in_range("velocity", vel, 0, 50)
    in_range("heading", head, -3.14, 3.14)
    return VehicleState(x=x, y=y, velocity=vel, heading=head)

# ---- model ----
class Model:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # real: load weights, move to device, eval()

    @torch.no_grad()
    def predict(self, ego: VehicleState, npcs: List[VehicleState], horizon: int):
        out = []
        for npc in npcs:
            out.append(VehicleState(
                x=npc.x + npc.velocity * horizon * 0.1,
                y=npc.y,
                velocity=npc.velocity,
                heading=npc.heading
            ))
        return out

model = Model()

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "gpu_available": torch.cuda.is_available()})

@app.post("/predict")
def predict():
    try:
        payload = request.get_json(force=True)

        ego = parse_vehicle(payload["ego_vehicle"])
        npcs = [parse_vehicle(v) for v in payload.get("npc_vehicles", [])]
        horizon = int(payload.get("prediction_horizon", 10))

        if horizon < 1 or horizon > 50:
            return jsonify({"detail": "prediction_horizon must be 1..50"}), 422
        if len(npcs) > 50:
            return jsonify({"detail": "Too many vehicles"}), 422

        start = time.perf_counter()
        preds = model.predict(ego, npcs, horizon)

        return jsonify({
            "request_id": str(uuid.uuid4()),
            "npc_next_states": [asdict(p) for p in preds],
            "computation_time_ms": (time.perf_counter() - start) * 1000
        })

    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"detail": str(e)}), 422
    except Exception:
        return jsonify({"detail": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
