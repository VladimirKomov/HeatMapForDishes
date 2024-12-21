from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal, get_db
from app.schemas import HeatMapRequest, HeatMapResponse, DataPoint
from app.services.heatmap import generate_heatmap_data

# create router
router = APIRouter()


@router.post("/heat-map-dishes", response_model=HeatMapResponse)
def heat_map_dishes(request: HeatMapRequest, db: Session = Depends(get_db)):
    response = generate_heatmap_data(db, request)
    return response
