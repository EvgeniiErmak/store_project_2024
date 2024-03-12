# tests/test_auth.py
from fastapi.testclient import TestClient
from app import create_app

client = TestClient(create_app)


def test_create_user():
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "email" in data
    assert "hashed_password" not in data


def test_login():
    response = client.post("/auth/login", data={"username": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "token_type" in data


def test_access_protected_route():
    response = client.get("/protected-route")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "You have access to this protected route"
