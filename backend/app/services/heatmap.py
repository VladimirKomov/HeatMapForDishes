from sqlalchemy.orm import Session
from app.schemas import HeatMapRequest, HeatMapResponse, DataPoint

def fetch_heatmap_data_from_db(db: Session, request: HeatMapRequest):

    data = [
        DataPoint(day="2024-12-01", hour=13, quantity=2, price_usd=2.25, total_sales_usd=4.5),
        DataPoint(day="2024-12-03", hour=18, quantity=1, price_usd=2.25, total_sales_usd=2.25),
    ]
    return data

def generate_insight(data):

    return "If you sell 5% more, your revenue will go up by 0.34$"

def generate_heatmap_data(db: Session, request: HeatMapRequest) -> HeatMapResponse:

    data = fetch_heatmap_data_from_db(db, request)
    insight = generate_insight(data)
    return HeatMapResponse(time_period=request.time_period, data=data, insight=insight)
