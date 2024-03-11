# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    image = Column(String)

    subcategories = relationship("Subcategory", back_populates="category")


class Subcategory(Base):
    __tablename__ = "subcategories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    image = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="subcategories")
    products = relationship("Product", back_populates="subcategory")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, index=True)
    price = Column(Integer)
    image_small = Column(String)
    image_medium = Column(String)
    image_large = Column(String)
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"))

    subcategory = relationship("Subcategory", back_populates="products")
