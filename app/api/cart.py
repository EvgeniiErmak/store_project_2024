# app/api/cart.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/cart/", response_model=schemas.Cart)
def create_cart_item(cart_item: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud.create_cart_item(db=db, cart_item=cart_item)


@router.get("/cart/", response_model=list[schemas.Cart])
def read_cart_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cart_items = crud.get_cart_items(db=db, skip=skip, limit=limit)
    return cart_items


@router.get("/cart/{cart_item_id}", response_model=schemas.Cart)
def read_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    cart_item = crud.get_cart_item(db=db, cart_item_id=cart_item_id)
    if cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return cart_item


@router.put("/cart/{cart_item_id}", response_model=schemas.Cart)
def update_cart_item(cart_item_id: int, cart_item: schemas.CartUpdate, db: Session = Depends(get_db)):
    return crud.update_cart_item(db=db, cart_item_id=cart_item_id, cart_item=cart_item)


@router.delete("/cart/{cart_item_id}", response_model=schemas.Cart)
def delete_cart_item(cart_item_id: int, db: Session = Depends(get_db)):
    return crud.delete_cart_item(db=db, cart_item_id=cart_item_id)
