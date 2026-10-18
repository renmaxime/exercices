from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_create_item():
    r = client.post("/items", json={"name": "Camille"})
    assert r.status_code == 201
    assert r.json()["name"] == "Camille"

def test_update_item():
    r = client.post("/items", json={"name": "Paul"})
    new_id = r.json()["id"]

    r = client.put(f"/items/{new_id}", json={"name": "Pierre"})
    assert r.status_code == 200
    assert r.json()["name"] == "Pierre"

def test_delete_item():
    r = client.post("/items", json={"name": "Camille"})
    new_id = r.json()["id"]

    r = client.delete(f"/items/{new_id}")
    assert r.status_code == 204

    r = client.get(f"/items/{new_id}")
    assert r.status_code == 404

def test_read_item():
    r = client.post("/items", json={"name": "Camille"})
    new_id = r.json()["id"]

    r = client.get(f"/items/{new_id}")
    assert r.status_code == 200
    assert r.json()["name"] == "Camille"


def test_item_not_found():
    r = client.get("/items/99999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Item not found"