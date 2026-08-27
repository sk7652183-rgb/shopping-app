# 🛍️ FastAPI Shopping App

A full-stack shopping application built with **Python FastAPI**, **SQLite**, **HTML/CSS/JavaScript**, **Docker**, and **GitHub Actions**.

The application provides a web-based shopping interface and REST APIs for managing products. It is also deployed on an **Ubuntu AWS EC2 instance** as part of the DevOps learning project.

---

## 🎥 Demo Video

### 📺 Application Demo

Watch the complete demonstration of the FastAPI Shopping App:

**▶️ [Watch Shopping App Demo]( 

https://github.com/user-attachments/assets/6ff207e4-1aa2-41d3-93bf-4cf6c761c52c

)**

> The demo covers the Shopping UI, product management, FastAPI REST APIs, SQLite database, Docker containerization, automated testing, GitHub Actions, and deployment on Ubuntu/AWS EC2.

### 🚀 Demo Flow

```text
                    Shopping App
                         │
                         ▼
                  Web Application
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
       View Products             Add Product
             │                       │
             │                       ▼
             │                SQLite Database
             │                       │
             └───────────┬───────────┘
                         ▼
                  FastAPI REST API
                         │
                         ▼
                  Docker Container
                         │
                         ▼
                  GitHub Actions
```

### 🎬 Demo Includes

* 🏠 Shopping application homepage
* 📦 Product listing
* ➕ Add new product
* 🔎 View product
* ✏️ Update product
* 🗑️ Delete product
* 💾 SQLite database
* 📡 FastAPI REST APIs
* 📚 Swagger UI
* 🐳 Docker containerization
* 🧪 Pytest automated testing
* ⚙️ GitHub Actions CI
* ☁️ Ubuntu/AWS EC2 deployment

---

## 🚀 Features

* Modern shopping web interface
* Product management
* Create products
* View all products
* View individual products
* Update products
* Delete products
* SQLite database
* FastAPI REST APIs
* Interactive Swagger documentation
* Automated testing with Pytest
* Docker containerization
* GitHub Actions CI pipeline
* Ubuntu server deployment
* AWS EC2 hosting

---

## 🏗️ Architecture

```text
                         Developer
                             │
                             │ git push
                             ▼
                    ┌─────────────────┐
                    │     GitHub      │
                    │   Repository    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    │      CI/CD      │
                    └────────┬────────┘
                             │
                     ┌───────┴────────┐
                     │                │
                     ▼                ▼
                Run Tests       Docker Build
                     │                │
                     └───────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Docker Image   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    AWS EC2      │
                    │     Ubuntu      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ FastAPI App     │
                    │     :8000       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     SQLite      │
                    │    Database     │
                    └─────────────────┘
```

---

## 🛠️ Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Python         | Application development |
| FastAPI        | Backend REST API        |
| SQLite         | Database                |
| HTML           | Web interface           |
| CSS            | UI styling              |
| JavaScript     | Frontend interaction    |
| Jinja2         | HTML templates          |
| Pytest         | Automated testing       |
| Docker         | Containerization        |
| GitHub Actions | CI/CD automation        |
| Ubuntu         | Server environment      |
| AWS EC2        | Cloud hosting           |
| Git            | Version control         |

---

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

---

## 📋 API Endpoints

| Method   | Endpoint         | Description             |
| -------- | ---------------- | ----------------------- |
| `GET`    | `/`              | Shopping application UI |
| `GET`    | `/products`      | Get all products        |
| `GET`    | `/products/{id}` | Get product by ID       |
| `POST`   | `/products`      | Create a product        |
| `PUT`    | `/products/{id}` | Update a product        |
| `DELETE` | `/products/{id}` | Delete a product        |

---

## 📦 Product API

### Create Product

**POST `/products`**

Request:

```json
{
  "name": "Laptop",
  "price": 65000,
  "category": "Electronics"
}
```

Response:

```json
{
  "id": 1,
  "message": "Product created successfully"
}
```

---

### Get All Products

**GET `/products`**

Example response:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 65000,
    "category": "Electronics"
  },
  {
    "id": 2,
    "name": "Headphones",
    "price": 2500,
    "category": "Electronics"
  }
]
```

---

### Get Product by ID

**GET `/products/1`**

Example response:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 65000,
  "category": "Electronics"
}
```

---

### Update Product

**PUT `/products/1`**

Request:

```json
{
  "name": "Gaming Laptop",
  "price": 75000,
  "category": "Electronics"
}
```

Response:

```json
{
  "message": "Product updated successfully"
}
```

---

### Delete Product

**DELETE `/products/1`**

Response:

```json
{
  "message": "Product deleted successfully"
}
```

---

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

Ubuntu/Linux:

```bash
source venv/bin/activate
```

Windows:

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

Application:

```text
http://localhost:8000
```

---

## 🌐 Access the Application on AWS EC2

When running on an Ubuntu EC2 instance:

```text
http://YOUR-EC2-PUBLIC-IP:8000
```

For example:

```text
http://YOUR-EC2-PUBLIC-IP:8000
```

Make sure TCP port `8000` is allowed in the EC2 Security Group.

### EC2 Security Group

```text
Type:      Custom TCP
Protocol:  TCP
Port:      8000
Source:    My IP
```

For temporary testing, `0.0.0.0/0` can be used, but restricting access to your IP is recommended.

---

## 📚 Swagger API Documentation

FastAPI provides interactive API documentation automatically.

Open:

```text
http://localhost:8000/docs
```

For EC2:

```text
http://YOUR-EC2-PUBLIC-IP:8000/docs
```

You can test all product APIs directly from Swagger UI.

---

## 🧪 Testing

The project uses **Pytest** for automated testing.

Run:

```bash
pytest -v
```

Example:

```text
============================= test session starts =============================

tests/test_main.py ...                                               [100%]

============================== 3 passed =======================================
```

---

## 🐳 Docker

### Build Docker Image

```bash
docker build -t shopping-app .
```

### Run Container

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

### Stop Container

```bash
docker stop shopping-container
```

### Remove Container

```bash
docker rm shopping-container
```

---

## ⚙️ GitHub Actions

The project uses **GitHub Actions** for continuous integration.

Workflow:

```text
.github/workflows/ci.yml
```

The pipeline performs:

```text
Git Push
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
Tests Passed
    │
    ▼
Build Docker Image
```

The Docker image is built only after the tests pass.

---

## 🔄 CI Pipeline

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
                 ┌─────┴─────┐
                 │           │
              Failed       Passed
                 │           │
                 ▼           ▼
                Stop    Docker Build
                            │
                            ▼
                       Docker Image
```

---

## ☁️ AWS EC2 Deployment

The application can be deployed on an Ubuntu AWS EC2 instance.

Deployment architecture:

```text
                        Internet
                           │
                           │ HTTP :8000
                           ▼
                  ┌──────────────────┐
                  │     AWS EC2      │
                  │      Ubuntu      │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Docker Container │
                  └────────┬─────────┘
                           │
                           ▼
                       FastAPI
                           │
                           ▼
                        SQLite
```

---

## 🔐 Security Considerations

For production deployment:

* Do not commit passwords or API keys.
* Use GitHub Secrets for sensitive credentials.
* Restrict EC2 Security Group access.
* Use HTTPS.
* Use environment variables for configuration.
* Avoid exposing unnecessary ports.
* Use PostgreSQL for larger production workloads.
* Use a reverse proxy such as Nginx.
* Keep dependencies updated.

---

## 📈 Future Improvements

Planned improvements include:

* 👤 User authentication
* 🔐 JWT authentication
* 🛒 Shopping cart
* ❤️ Wishlist
* 💳 Payment integration
* 📦 Order management
* 🐘 PostgreSQL
* 🔴 Redis caching
* 🌐 Nginx reverse proxy
* 🔒 HTTPS/SSL
* 🐳 Docker Compose
* 🚀 Automated deployment
* ☸️ Kubernetes deployment
* 📊 Monitoring
* 📝 Centralized logging
* ❤️ Health checks

---

## 🎯 DevOps Learning Goals

This project demonstrates practical experience with:

* Linux/Ubuntu
* Python
* FastAPI
* REST APIs
* SQLite
* Git
* GitHub
* Docker
* Dockerfile
* Container management
* Automated testing
* GitHub Actions
* CI/CD
* AWS EC2
* Application deployment

---

## 👨‍💻 Author

**Abusufiyan Khan**

DevOps / Cloud / Infrastructure Enthusiast

---

## 📄 License

This project is created for learning and demonstration purposes.
