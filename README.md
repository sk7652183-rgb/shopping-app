# 🛍️ FastAPI Shopping App

A simple full-stack shopping application built with **Python FastAPI**, **SQLite**, **HTML/CSS/JavaScript**, **Docker**, and **GitHub Actions**.

The application provides a web-based shopping UI along with REST APIs for managing products.

## 🚀 Features

* 🛍️ Shopping web interface
* 📦 Product management
* ➕ Add products
* 🔍 View all products
* 🔎 Get a product by ID
* ✏️ Update products
* 🗑️ Delete products
* 💾 SQLite database
* 📡 FastAPI REST APIs
* 📚 Swagger API documentation
* 🐳 Docker containerization
* 🧪 Automated testing with Pytest
* ⚙️ GitHub Actions CI pipeline

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │      Browser     │
                    │   Shopping UI    │
                    └────────┬─────────┘
                             │
                             │ HTTP :8000
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │   Application    │
                    └────────┬─────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
        ┌──────────────┐          ┌──────────────┐
        │  REST APIs   │          │    SQLite    │
        │  /products   │          │   Database   │
        └──────────────┘          └──────────────┘
```

## 📁 Project Structure

```text
shopping-app/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── style.css
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## 🛠️ Technologies Used

| Technology     | Purpose                  |
| -------------- | ------------------------ |
| Python         | Application programming  |
| FastAPI        | Backend REST API         |
| SQLite         | Database                 |
| HTML           | Web UI                   |
| CSS            | UI styling               |
| JavaScript     | Frontend API interaction |
| Pytest         | Automated testing        |
| Docker         | Containerization         |
| GitHub Actions | CI/CD automation         |
| Ubuntu         | Application hosting      |

## 📋 API Endpoints

| Method | Endpoint         | Description             |
| ------ | ---------------- | ----------------------- |
| GET    | `/`              | Shopping application UI |
| GET    | `/products`      | Get all products        |
| GET    | `/products/{id}` | Get product by ID       |
| POST   | `/products`      | Create a product        |
| PUT    | `/products/{id}` | Update a product        |
| DELETE | `/products/{id}` | Delete a product        |

## 📦 Product Example

### Create Product

**POST `/products`**

```json
{
  "name": "Laptop",
  "price": 65000,
  "category": "Electronics"
}
```

Example response:

```json
{
  "id": 1,
  "message": "Product created successfully"
}
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd shopping-app
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

For Ubuntu/Linux:

```bash
source venv/bin/activate
```

For Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The application will be available at:

```text
http://localhost:8000
```

## 📚 Swagger Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://localhost:8000/docs
```

You can test all product APIs directly from Swagger UI.

## 🧪 Run Tests

Run the automated tests with:

```bash
pytest -v
```

Example:

```text
============================= test session starts =============================
collected 3 items

tests/test_main.py ...                                                [100%]

============================== 3 passed =======================================
```

## 🐳 Run with Docker

### Build the Docker image

```bash
docker build -t shopping-app .
```

### Run the container

```bash
docker run -d \
  --name shopping-container \
  -p 8000:8000 \
  shopping-app
```

Check the running container:

```bash
docker ps
```

Open:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

### Stop the container

```bash
docker stop shopping-container
```

### Remove the container

```bash
docker rm shopping-container
```

## ⚙️ GitHub Actions CI/CD

The project includes a GitHub Actions workflow:

```text
.github/workflows/ci.yml
```

The CI pipeline performs:

```text
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Checkout Code
    │
    ▼
Setup Python
    │
    ▼
Install Dependencies
    │
    ▼
Run Pytest
    │
    ▼
Build Docker Image
```

The Docker build runs only after the tests successfully pass.

## 🔄 CI Workflow

```yaml
test
  │
  ├── Checkout Code
  ├── Setup Python
  ├── Install Dependencies
  └── Run Tests
          │
          ▼
     Tests Passed
          │
          ▼
    Docker Build
```

## ☁️ Deployment

The application can be deployed to an Ubuntu server or AWS EC2 instance.

Example architecture:

```text
Developer
    │
    │ git push
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Run Tests
    ├── Build Docker Image
    │
    ▼
Docker Image
    │
    ▼
AWS EC2 / Ubuntu
    │
    ▼
FastAPI Container
    │
    ▼
Shopping App
```

## 🔐 Security Considerations

For production deployment:

* Do not commit secrets to GitHub.
* Use GitHub Secrets for credentials.
* Restrict EC2 Security Group access.
* Use HTTPS with a reverse proxy.
* Avoid exposing unnecessary ports.
* Use environment variables for configuration.
* Use a production-grade database for larger workloads.

## 📈 Future Improvements

The application can be extended with:

* 👤 User authentication
* 🛒 Shopping cart
* ❤️ Wishlist
* 💳 Payment integration
* 📦 Order management
* 🔐 JWT authentication
* 🐘 PostgreSQL
* 🔴 Redis caching
* 🌐 Nginx reverse proxy
* 🔒 HTTPS/SSL
* 🐳 Docker Compose
* 🚀 Automated deployment
* ☸️ Kubernetes deployment
* 🔍 Monitoring and logging

## 👨‍💻 DevOps Learning Goals

This project is designed to demonstrate practical DevOps concepts including:

* Git and GitHub
* Linux/Ubuntu
* Python application deployment
* REST APIs
* Docker
* Container management
* Automated testing
* GitHub Actions
* CI/CD pipelines
* AWS EC2 deployment

## 📄 License

This project is for learning and demonstration purposes.
