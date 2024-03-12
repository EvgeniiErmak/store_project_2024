# tests/test_subcategories.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_subcategory():
    response = client.post("/subcategories/", json={"name": "Test Subcategory", "slug": "test-subcategory", "category_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Subcategory"
    assert data["slug"] == "test-subcategory"


def test_read_subcategories():
    response = client.get("/subcategories/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_subcategory():
    # Assuming subcategory with ID 1 exists
    response = client.get("/subcategories/1")
    assert response.status_code == 200
    data = response.json()
    assert data.get("id") == 1


def test_update_subcategory():
    # Assuming subcategory with ID 1 exists
    response = client.put("/subcategories/1", json={"name": "Updated Subcategory", "slug": "updated-subcategory", "category_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Subcategory"
    assert data["slug"] == "updated-subcategory"


def test_delete_subcategory():
    # Assuming subcategory with ID 1 exists
    response = client.delete("/subcategories/1")
    assert response.status_code == 200
    data = response.json()
    assert data.get("id") == 1
