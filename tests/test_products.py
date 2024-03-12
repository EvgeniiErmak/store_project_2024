# tests/test_products.py
from fastapi.testclient import TestClient
from app.database import engine
from app.main import app
from app import models

client = TestClient(app)


def test_create_product():
    response = client.post("/products/", json={"name": "Test Product", "slug": "test-product", "price": 100})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "slug" in data
    assert "price" in data


def test_read_products():
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_product():
    # Assuming product with ID 1 exists
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "slug" in data
    assert "price" in data


def test_update_product():
    # Assuming product with ID 1 exists
    response = client.put("/products/1", json={"name": "Updated Product", "slug": "updated-product"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["slug"] == "updated-product"


def test_delete_product():
    # Assuming product with ID 1 exists
    response = client.delete("/products/1")
    assert response.status_code == 200
