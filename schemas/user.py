from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    location_lat: float
    location_lon: float

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    location_lat: float
    location_lon: float

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str