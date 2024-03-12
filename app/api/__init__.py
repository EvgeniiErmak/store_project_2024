# app/api/__init__.py
from . import categories, subcategories, cart
from fastapi import APIRouter
from . import categories, subcategories, cart
from . import cart, categories, subcategories, products

api_router = APIRouter()

api_router.include_router(cart.router, prefix="/cart", tags=["cart"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(subcategories.router, prefix="/subcategories", tags=["subcategories"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
