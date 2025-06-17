# 📝 FastAPI Blog API

A **secure, modular, and scalable Blog API** built with **FastAPI**, **SQLAlchemy**, and **JWT Authentication**.

Designed for professional developers and learners to explore:
- FastAPI route building
- JWT authentication
- Database relationships using SQLAlchemy ORM
- Dependency injection
- Token-based access control

---

## 🚀 Features

- ✅ User Registration & Login (JWT Auth)
- 🛡️ Protected Routes (Create, Update, Delete blogs only if logged in)
- 📄 Public Endpoints to Read Blogs
- ✏️ Only Owner Can Edit/Delete Their Blog
- 🧠 Clean code architecture (Routers, Schemas, Models, Auth, DB)
- 📦 Modular and Scalable project structure

---

## 🧪 Tech Stack

| Layer         | Technology             |
|---------------|------------------------|
| ⚙️ Framework  | [FastAPI](https://fastapi.tiangolo.com) |
| 🧠 ORM        | [SQLAlchemy](https://www.sqlalchemy.org/) |
| 🗃️ Database   | SQLite (Dev) / PostgreSQL (Prod-ready) |
| 🔐 Auth       | JWT (OAuth2 password flow) |
| 📦 Validation | Pydantic |
| 🧪 Testing    | Swagger UI (built-in) |
| 🖥️ Docs       | Swagger + Redoc auto-generated |

---

## 📁 Project Structure

app/
├── main.py # FastAPI app entrypoint
├── database.py # DB connection & session
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic models
├── hashing.py # Password hashing (bcrypt)
├── jwt_handler.py # JWT token generation
├── auth.py # Current user dependency
├── routers/
│ ├── auth_routes.py # Register & Login
│ └── blog_routes.py # CRUD Blog APIs



---

## 📦 Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/zainchodry/fastapi-blog-api.git
cd fastapi-blog-api

#Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


# Install Dependencies
pip install -r requirements.txt

# Run the Server
uvicorn app.main:app --reload

