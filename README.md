# FastAPI Example Project

This project demonstrates a simple FastAPI application with user CRUD endpoints and background tasks.

## Features
- Create, read, and delete users
- Welcome email background task (simulated)
- JWT-based authentication for delete endpoint (mocked in tests)
- SQLite database with SQLAlchemy ORM
- Pydantic models for request/response validation
- Automated tests for all endpoints

## Requirements
- Python 3.12+
- [pip](https://pip.pypa.io/en/stable/)

## Setup

1. **Clone the repository**

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic jwt
   ```

4. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at http://127.0.0.1:8000

5. **Interactive API docs**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Running Tests

Tests are in `test_app.py` and use FastAPI's `TestClient`.

```bash
pytest test_app.py
```

## Endpoints
- `POST /users/` — Create a user
- `GET /users/` — List users
- `GET /users/{user_id}` — Get user by ID
- `DELETE /users/{user_id}` — Delete user (requires JWT, mocked in tests)
- `POST /welcome/` — Schedule welcome email (background task)

## Notes
- The delete endpoint requires a JWT token. In tests, the dependency is mocked.
- The welcome email is simulated with a print statement.
- The database is SQLite and will create a `test.db` file in the project directory.

---
