# app/__init__.py
from fastapi import FastAPI
from app.api import cart, categories, products, subcategories


def create_app():
    app = FastAPI()
    app.include_router(cart.router)
    app.include_router(categories.router)
    app.include_router(products.router)
    app.include_router(subcategories.router)
    return app


def app(scope, receive, send):
    return create_app()(scope, receive, send)
