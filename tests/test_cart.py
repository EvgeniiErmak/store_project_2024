# tests/test_cart.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_cart_item():
    response = client.post("/cart/", json={"product_id": 1, "quantity": 2})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "product_id" in data
    assert "quantity" in data


def test_read_cart_items():
    response = client.get("/cart/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_cart_item():
    # Assuming cart item with ID 1 exists
    response = client.get("/cart/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "product_id" in data
    assert "quantity" in data


def test_update_cart_item():
    # Assuming cart item with ID 1 exists
    response = client.put("/cart/1", json={"quantity": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 3


def test_delete_cart_item():
    # Assuming cart item with ID 1 exists
    response = client.delete("/cart/1")
    assert response.status_code == 200
