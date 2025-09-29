from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from utils.databases import engine, get_db
from models import base, user, resturant, product, order
from auth.router import router as auth_router
from routes.users import router as users_router
from routes.resturants import router as restaurants_router
from routes.products import router as products_router
from routes.orders import router as orders_router
from routes.search import router as search_router
import random

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables
    base.Base.metadata.create_all(bind=engine)
    
    # Seed dummy data
    seed_dummy_data()
    yield

app = FastAPI(
    title="Food Ordering API",
    description="A Zomato-like food ordering system",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(auth_router)
app.include_router(restaurants_router)
app.include_router(products_router)
app.include_router(users_router)
app.include_router(orders_router)
app.include_router(search_router)

def seed_dummy_data():
    from utils.databases import SessionLocal
    from utils.password import hash_password
    from models.user import User
    from models.resturant import Restaurant
    from models.product import Product
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(User).count() == 0:
            # Seed users
            users = [
                User(name="John Doe", email="john@example.com", 
                     password_hash=hash_password("password123"), 
                     location_lat=12.9716, location_lon=77.5946),
                User(name="Jane Smith", email="jane@example.com", 
                     password_hash=hash_password("password123"), 
                     location_lat=12.9352, location_lon=77.6245),
            ]
            db.add_all(users)
            db.commit()
        
        if db.query(Restaurant).count() == 0:
            # Seed restaurants
            restaurants = [
                Restaurant(name="Pizza Palace", location_lat=12.9716, location_lon=77.5946, rating=4.2),
                Restaurant(name="Burger King", location_lat=12.9352, location_lon=77.6245, rating=4.0),
                Restaurant(name="Sushi House", location_lat=12.9234, location_lon=77.5678, rating=4.5),
            ]
            db.add_all(restaurants)
            db.commit()
        
        if db.query(Product).count() == 0:
            # Seed products
            products = []
            for restaurant_id in range(1, 4):
                for i in range(5):
                    products.append(Product(
                        restaurant_id=restaurant_id,
                        name=f"Product {i+1} from Restaurant {restaurant_id}",
                        price=round(random.uniform(5.0, 30.0), 2),
                        popularity_score=round(random.uniform(3.0, 5.0), 1)
                    ))
            
            db.add_all(products)
            db.commit()
    
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Food Ordering API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)