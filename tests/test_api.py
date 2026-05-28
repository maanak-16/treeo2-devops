from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "TreeO2 Backend API is running"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.json()["monitoring"] == "enabled"


def test_trees():
    response = client.get("/trees")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_farmers():
    response = client.get("/farmers")
    assert response.status_code == 200
    assert len(response.json()) > 0