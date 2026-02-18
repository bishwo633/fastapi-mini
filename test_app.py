from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "alice", "email": "alice@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"

def test_read_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404

# Test for GET /users/
def test_read_users():
    client.post("/users/", json={"username": "bob", "email": "bob@example.com"})
    client.post("/users/", json={"username": "carol", "email": "carol@example.com"})
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(user["username"] == "bob" for user in data)
    assert any(user["username"] == "carol" for user in data)

# Test for GET /users/{user_id}
def test_read_user():
    create_resp = client.post("/users/", json={"username": "dave", "email": "dave@example.com"})
    user_id = create_resp.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "dave"
    assert data["email"] == "dave@example.com"

# Test for DELETE /users/{user_id}
def test_delete_user():
    create_resp = client.post("/users/", json={"username": "eve", "email": "eve@example.com"})
    user_id = create_resp.json()["id"]
    import main
    main.get_current_user = lambda: "dummy"
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["msg"] == "User deleted"
    get_resp = client.get(f"/users/{user_id}")
    assert get_resp.status_code == 404

# Test for POST /welcome/
def test_welcome_user():
    response = client.post("/welcome/", json={"username": "frank", "email": "frank@example.com"})
    assert response.status_code == 200
    assert "Welcome email scheduled for frank@example.com" in response.json()["msg"]
