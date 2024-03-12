# app/schemas.py
from typing import List, Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str


class CategoryBase(BaseModel):
    name: str
    slug: str
    image: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    subcategories: List["Subcategory"] = []

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    slug: str
    price: int
    image_small: Optional[str] = None
    image_medium: Optional[str] = None
    image_large: Optional[str] = None
    subcategory_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


class SubcategoryBase(BaseModel):
    name: str
    slug: str
    image: Optional[str] = None
    category_id: int
    products: List[Product] = []


class SubcategoryCreate(SubcategoryBase):
    pass


class SubcategoryUpdate(SubcategoryBase):
    pass


class Subcategory(SubcategoryBase):
    id: int
    products: List[Product] = []

    class Config:
        from_attributes = True


class Cart:
    pass


class CartUpdate:
    pass


class CartCreate:
    pass