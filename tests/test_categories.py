# tests/test_categories.py
from fastapi.testclient import TestClient
from app.database import engine
from app.main import app
from app import models

client = TestClient(app)


def test_create_category():
    response = client.post("/categories/", json={"name": "Test Category", "slug": "test-category"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"
    assert data["slug"] == "test-category"
    assert "id" in data


def test_read_categories():
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_read_category():
    # Assuming category with ID 1 exists
    response = client.get("/categories/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "slug" in data


def test_update_category():
    # Assuming category with ID 1 exists
    response = client.put("/categories/1", json={"name": "Updated Category", "slug": "updated-category"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Category"
    assert data["slug"] == "updated-category"


def test_delete_category():
    # Assuming category with ID 1 exists
    response = client.delete("/categories/1")
    assert response.status_code == 200
