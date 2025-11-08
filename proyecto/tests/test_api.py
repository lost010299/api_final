from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    data = {"name": "Monitor", "value": 150.0}
    r = client.post("/api/items", json=data)
    assert r.status_code == 201
    res = r.json()
    assert res["name"] == "Monitor"
    assert "id" in res

def test_validation_error():
    data = {"name": "", "value": 10}
    r = client.post("/api/items", json=data)
    assert r.status_code == 422

def test_item_not_found():
    r = client.get("/api/items/999")
    assert r.status_code == 404
    assert "error" in r.json()["detail"]