
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.database import get_connection, init_db


# Create FastAPI application
app = FastAPI(title="Shopping App")


# Initialize database
init_db()


# Serve CSS, JavaScript, images, etc.
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


# Configure HTML templates
templates = Jinja2Templates(directory="app/templates")


# --------------------------------------------------
# PRODUCT MODEL
# --------------------------------------------------

class Product(BaseModel):
    name: str
    price: float
    category: str


# --------------------------------------------------
# HOME PAGE / UI
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# GET ALL PRODUCTS
# --------------------------------------------------

@app.get("/products")
def get_products():
    connection = get_connection()

    products = connection.execute(
        "SELECT * FROM products"
    ).fetchall()

    connection.close()

    return [dict(product) for product in products]


# --------------------------------------------------
# GET PRODUCT BY ID
# --------------------------------------------------

@app.get("/products/{product_id}")
def get_product(product_id: int):
    connection = get_connection()

    product = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    connection.close()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return dict(product)


# --------------------------------------------------
# CREATE PRODUCT
# --------------------------------------------------

@app.post("/products")
def create_product(product: Product):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO products
        (name, price, category)
        VALUES (?, ?, ?)
        """,
        (
            product.name,
            product.price,
            product.category
        )
    )

    connection.commit()

    product_id = cursor.lastrowid

    connection.close()

    return {
        "id": product_id,
        "message": "Product created successfully"
    }


# --------------------------------------------------
# UPDATE PRODUCT
# --------------------------------------------------

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    connection = get_connection()

    existing = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    if existing is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    connection.execute(
        """
        UPDATE products
        SET name = ?,
            price = ?,
            category = ?
        WHERE id = ?
        """,
        (
            product.name,
            product.price,
            product.category,
            product_id
        )
    )

    connection.commit()

    connection.close()

    return {
        "message": "Product updated successfully"
    }


# --------------------------------------------------
# DELETE PRODUCT
# --------------------------------------------------

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    connection = get_connection()

    existing = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    if existing is None:
        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    connection.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    connection.commit()

    connection.close()

    return {
        "message": "Product deleted successfully"
    }

