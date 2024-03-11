# app/api/__init__.py
from fastapi import APIRouter
from . import categories, products, cart
from . import categories, products, cart

api_router = APIRouter()

api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(cart.router, prefix="/cart", tags=["cart"])
