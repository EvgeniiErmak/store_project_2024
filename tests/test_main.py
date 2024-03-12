# tests/test_main.py
from fastapi.testclient import TestClient
from app import create_app

client = TestClient(create_app())


def test_app():
    response = client.get("/")
    assert response.status_code == 404
