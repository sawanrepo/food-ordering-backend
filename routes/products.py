from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.databases import get_db
from models.product import Product
from schemas.product import ProductResponse
from dsa.hash_map import HashMap

router = APIRouter(prefix="/products", tags=["Products"])
product_hash_map = HashMap()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    cached_product = product_hash_map.get(product_id)
    if cached_product:
        return cached_product
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_response = ProductResponse.from_orm(product)
    product_hash_map.put(product_id, product_response)
    
    return product_response