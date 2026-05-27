from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_aeroporti():
    response = client.get("/")
    assert response.status_code == 200

def test_get_aeroporto():
    response = client.get("/1")
    assert response.status_code == 200

def test_create_aeroporto():
    data = {
        "codice": "FCO",
        "citta": "Roma"
    }
    response = client.post("/", json=data)
    assert response.status_code == 201