from pydantic import BaseModel

class ProductCreate(BaseModel):
    restaurant_id: int
    name: str
    price: float
    popularity_score: float = 0.0

class ProductResponse(BaseModel):
    id: int
    restaurant_id: int
    name: str
    price: float
    popularity_score: float

    class Config:
        from_attributes = True