from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    restaurant_id: int
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    items: List[Dict]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True