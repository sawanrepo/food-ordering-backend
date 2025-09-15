from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from utils.databases import get_db
from models.resturant import Restaurant
from models.product import Product
from schemas.resturant import RestaurantResponse
from schemas.product import ProductResponse

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/restaurants")
def search_restaurants(query: str, db: Session = Depends(get_db)):
    restaurants = db.query(Restaurant).filter(
        Restaurant.name.ilike(f"%{query}%")
    ).all()
    
    return [RestaurantResponse.from_orm(restaurant) for restaurant in restaurants]

@router.get("/products")
def search_products(query: str, db: Session = Depends(get_db)):
    products = db.query(Product).filter(
        Product.name.ilike(f"%{query}%")
    ).all()
    
    return [ProductResponse.from_orm(product) for product in products]