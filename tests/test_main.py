"""doc string"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """doc string"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hell on World"}

def test_read_data():
    """doc string"""
    response = client.get("/data/ion")
    assert response.status_code == 200
    assert response.json() == {"message":"Hell on World ion"}
    