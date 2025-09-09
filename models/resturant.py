from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Restaurant(Base):
    _tablename_ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location_lat = Column(Float, nullable=False)
    location_lon = Column(Float, nullable=False)
    rating = Column(Float, default=0.0)