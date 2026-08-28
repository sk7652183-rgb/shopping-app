# This file is for testing purposes and contains the test cases.

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_create_product(client):
    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 65000,
            "category": "Electronics"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Product created successfully"


def test_get_products(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
