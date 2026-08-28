# This file is for Testing purpose 
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Shopping App API is running"


def test_create_product():
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


def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
