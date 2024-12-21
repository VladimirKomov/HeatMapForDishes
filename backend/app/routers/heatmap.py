from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.schemas import HeatMapRequest, HeatMapResponse, DataPoint

# create router
router = APIRouter()


# Dependency for creating a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_heatmap_data(request: HeatMapRequest) -> HeatMapResponse:
    data = [
        DataPoint(day="2024-12-01", hour=13, quantity=2, price_usd=2.25, total_sales_usd=4.5),
        DataPoint(day="2024-12-03", hour=18, quantity=1, price_usd=2.25, total_sales_usd=2.25),
    ]
    insight = "If you sell 5% more, your revenue will go up by 0.34$"
    return HeatMapResponse(time_period=request.time_period, data=data, insight=insight)


@router.post("/heat-map-dishes", response_model=HeatMapResponse)
def heat_map_dishes(request: HeatMapRequest, db: Session = Depends(get_db)):
    response = generate_heatmap_data(request)
    return response
