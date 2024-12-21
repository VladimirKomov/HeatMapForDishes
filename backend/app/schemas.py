from pydantic import BaseModel
from typing import List, Optional


class TimePeriod(BaseModel):
    start: str
    end: str


class HeatMapRequest(BaseModel):
    business_id: str
    dish_id: str
    time_period: TimePeriod


class DataPoint(BaseModel):
    day: str
    hour: int
    quantity: int
    price_usd: float
    total_sales_usd: float


class HeatMapResponse(BaseModel):
    time_period: TimePeriod
    data: List[DataPoint]
    insight: str
