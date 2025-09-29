from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .base import Base
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    popularity_score = Column(Float, default=0.0)