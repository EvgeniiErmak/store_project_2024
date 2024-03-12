# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_category():
    response = client.post("/categories/", json={"name": "Test Category", "slug": "test-category"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"
    assert data["slug"] == "test-category"


def test_get_categories():
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_create_subcategory():
    response = client.post("/subcategories/", json={"name": "Test Subcategory", "slug": "test-subcategory", "category_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Subcategory"
    assert data["slug"] == "test-subcategory"


def test_get_subcategories():
    response = client.get("/subcategories/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "slug": "test-product", "price": 100, "subcategory_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["slug"] == "test-product"


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_create_cart_item():
    response = client.post("/cart/", json={"user_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 1


def test_get_cart_items():
    response = client.get("/cart/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
