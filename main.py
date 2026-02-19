from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import torch
import uuid
from datetime import datetime

app = FastAPI()

# Models
class VehicleState(BaseModel):
    x: float = Field(..., ge=-1000, le=1000)
    y: float = Field(..., ge=-1000, le=1000)
    velocity: float = Field(..., ge=0, le=50)
    heading: float = Field(..., ge=-3.14, le=3.14)

class PredictionRequest(BaseModel):
    ego_vehicle: VehicleState
    npc_vehicles: List[VehicleState]
    prediction_horizon: int = Field(default=10, ge=1, le=50)

class PredictionResponse(BaseModel):
    request_id: str
    predictions: List[VehicleState]
    computation_time_ms: float

# Mock model (in production, load real model)
class Model:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
    
    @torch.no_grad()
    def predict(self, ego, npcs, horizon):
        # Mock prediction logic
        predictions = []
        for npc in npcs:
            # Simple prediction: continue at current velocity
            pred = VehicleState(
                x=npc.x + npc.velocity * horizon * 0.1,
                y=npc.y,
                velocity=npc.velocity,
                heading=npc.heading
            )
            predictions.append(pred)
        return predictions

model = Model()

# Routes
@app.get("/health")
def health():
    return {"status": "healthy", "gpu_available": torch.cuda.is_available()}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        import time
        start = time.time()
        
        # Validate
        if len(request.npc_vehicles) > 50:
            raise HTTPException(status_code=422, detail="Too many vehicles")
        
        # Predict
        predictions = model.predict(
            request.ego_vehicle,
            request.npc_vehicles,
            request.prediction_horizon
        )
        
        # Response
        return PredictionResponse(
            request_id=str(uuid.uuid4()),
            predictions=predictions,
            computation_time_ms=(time.time() - start) * 1000
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)