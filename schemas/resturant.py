from pydantic import BaseModel
from typing import List

class RestaurantCreate(BaseModel):
    name: str
    location_lat: float
    location_lon: float
    rating: float = 0.0

class RestaurantResponse(BaseModel):
    id: int
    name: str
    location_lat: float
    location_lon: float
    rating: float

    class Config:
        from_attributes = True
        