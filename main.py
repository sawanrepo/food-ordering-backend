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
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables
    base.Base.metadata.create_all(bind=engine)
    
    yield

app = FastAPI(
    title="Food Ordering API",
    description="A Zomato-like food ordering system",
    version="1.0.0",
    lifespan=lifespan
)

origins = [
    "http://localhost:3000", 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(restaurants_router)
app.include_router(products_router)
app.include_router(users_router)
app.include_router(orders_router)
app.include_router(search_router)

@app.get("/")
def root():
    return {"message": "Food Ordering API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)