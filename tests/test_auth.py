# tests/test_auth.py
from fastapi.testclient import TestClient
from app import create_app
from app.database import engine
from app.models import Base


client = TestClient(create_app())


def setup_function():
    Base.metadata.create_all(bind=engine)


def teardown_function():
    Base.metadata.drop_all(bind=engine)


def test_create_user():
    response = client.post("/register", json={"email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"


def test_login():
    # Assuming you have implemented a login endpoint
    response = client.post("/login", data={"username": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_access_protected_route():
    # Assuming you have implemented a protected route
    response = client.get("/protected-route")
    assert response.status_code == 401

    # Obtain token
    token_response = client.post("/login", data={"username": "test@example.com", "password": "testpassword"})
    access_token = token_response.json()["access_token"]

    # Access protected route with token
    response_with_token = client.get("/protected-route", headers={"Authorization": f"Bearer {access_token}"})
    assert response_with_token.status_code == 200
