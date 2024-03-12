# tests/test_crud.py
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal


def test_create_category(db: Session = SessionLocal()):
    category = schemas.CategoryCreate(name="Test Category", slug="test-category")
    created_category = crud.create_category(db=db, category=category)
    assert created_category.name == "Test Category"
    assert created_category.slug == "test-category"


def test_get_categories(db: Session = SessionLocal()):
    categories = crud.get_categories(db=db)
    assert isinstance(categories, list)


def test_create_subcategory(db: Session = SessionLocal()):
    subcategory = schemas.SubcategoryCreate(name="Test Subcategory", slug="test-subcategory", category_id=1)
    created_subcategory = crud.create_subcategory(db=db, subcategory=subcategory)
    assert created_subcategory.name == "Test Subcategory"
    assert created_subcategory.slug == "test-subcategory"


def test_get_subcategories(db: Session = SessionLocal()):
    subcategories = crud.get_subcategories(db=db)
    assert isinstance(subcategories, list)


def test_create_product(db: Session = SessionLocal()):
    product = schemas.ProductCreate(name="Test Product", slug="test-product", price=100, subcategory_id=1)
    created_product = crud.create_product(db=db, product=product)
    assert created_product.name == "Test Product"
    assert created_product.slug == "test-product"


def test_get_products(db: Session = SessionLocal()):
    products = crud.get_products(db=db)
    assert isinstance(products, list)


def test_create_cart_item(db: Session = SessionLocal()):
    cart_item = schemas.CartCreate(user_id=1)
    created_cart_item = crud.create_cart_item(db=db, cart_item=cart_item)
    assert created_cart_item.user_id == 1


def test_get_cart_items(db: Session = SessionLocal()):
    cart_items = crud.get_cart_items(db=db)
    assert isinstance(cart_items, list)
