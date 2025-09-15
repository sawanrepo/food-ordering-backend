from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from utils.databases import get_db
from models.resturant import Restaurant
from models.product import Product
from schemas.resturant import RestaurantResponse
from schemas.product import ProductResponse
from dsa.min_heap import MinHeap
from dsa.max_heap import MaxHeap

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.get("/", response_model=List[RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()

@router.get("/{restaurant_id}/menu")
def get_restaurant_menu(restaurant_id: int, sort_by: str = "price", db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.restaurant_id == restaurant_id).all()
    
    if sort_by == "price":
        heap = MinHeap()
        for product in products:
            heap.insert(product.price, product)
        
        sorted_products = []
        while not heap.is_empty():
            sorted_products.append(heap.extract_min()[1])
    
    elif sort_by == "popularity":
        heap = MaxHeap()
        for product in products:
            heap.insert(product.popularity_score, product)
        
        sorted_products = []
        while not heap.is_empty():
            sorted_products.append(heap.extract_max()[1])
    
    else:
        sorted_products = products
    
    return [ProductResponse.from_orm(product) for product in sorted_products]