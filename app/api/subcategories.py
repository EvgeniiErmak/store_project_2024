# app/api/subcategories.py
from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app import crud, schemas
from typing import List

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/subcategories/", response_model=schemas.Subcategory)
def create_subcategory(subcategory: schemas.SubcategoryCreate, db: Session = Depends(get_db)):
    return crud.create_subcategory(db=db, subcategory=subcategory)


@router.get("/subcategories/", response_model=List[schemas.Subcategory])
def read_subcategories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    subcategories = crud.get_subcategories(db=db, skip=skip, limit=limit)
    return subcategories


@router.get("/subcategories/{subcategory_id}", response_model=schemas.Subcategory)
def read_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory = crud.get_subcategory(db=db, subcategory_id=subcategory_id)
    if subcategory is None:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return subcategory


@router.put("/subcategories/{subcategory_id}", response_model=schemas.Subcategory)
def update_subcategory(subcategory_id: int, subcategory: schemas.SubcategoryUpdate, db: Session = Depends(get_db)):
    return crud.update_subcategory(db=db, subcategory_id=subcategory_id, subcategory=subcategory)


@router.delete("/subcategories/{subcategory_id}", response_model=schemas.Subcategory)
def delete_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    return crud.delete_subcategory(db=db, subcategory_id=subcategory_id)
