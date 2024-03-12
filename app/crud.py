# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas


def create_cart_item(db: Session, cart_item: schemas.CartCreate):
    db_cart_item = models.Cart(**cart_item.dict())
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item


def get_cart_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Cart).offset(skip).limit(limit).all()


def get_cart_item(db: Session, cart_item_id: int):
    return db.query(models.Cart).filter(models.Cart.id == cart_item_id).first()


def update_cart_item(db: Session, cart_item_id: int, cart_item: schemas.CartUpdate):
    db_cart_item = db.query(models.Cart).filter(models.Cart.id == cart_item_id).first()
    if db_cart_item:
        for key, value in cart_item.dict().items():
            setattr(db_cart_item, key, value)
        db.commit()
        db.refresh(db_cart_item)
    return db_cart_item


def delete_cart_item(db: Session, cart_item_id: int):
    db_cart_item = db.query(models.Cart).filter(models.Cart.id == cart_item_id).first()
    if db_cart_item:
        db.delete(db_cart_item)
        db.commit()
    return db_cart_item


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        for key, value in category.dict().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category


def create_subcategory(db: Session, subcategory: schemas.SubcategoryCreate):
    db_subcategory = models.Subcategory(**subcategory.dict())
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory


def get_subcategories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Subcategory).offset(skip).limit(limit).all()


def get_subcategory(db: Session, subcategory_id: int):
    return db.query(models.Subcategory).filter(models.Subcategory.id == subcategory_id).first()


def update_subcategory(db: Session, subcategory_id: int, subcategory: schemas.SubcategoryUpdate):
    db_subcategory = db.query(models.Subcategory).filter(models.Subcategory.id == subcategory_id).first()
    if db_subcategory:
        for key, value in subcategory.dict().items():
            setattr(db_subcategory, key, value)
        db.commit()
        db.refresh(db_subcategory)
    return db_subcategory


def delete_subcategory(db: Session, subcategory_id: int):
    db_subcategory = db.query(models.Subcategory).filter(models.Subcategory.id == subcategory_id).first()
    if db_subcategory:
        db.delete(db_subcategory)
        db.commit()
    return db_subcategory
