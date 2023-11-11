"""Module docstring"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """funtion docstring"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello World"}

def test_read_data():
    """funtion docstring"""
    response = client.get("/data/ion")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello World Ion"}
