from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from .base import Base

class Order(Base):
    _tablename_ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    items = Column(JSON, nullable=False)  # List of product IDs and quantities
    status = Column(String, default="pending")  # pending, preparing, delivered, cancelled
    created_at = Column(DateTime, server_default=func.now())