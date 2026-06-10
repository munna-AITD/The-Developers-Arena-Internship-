from fastapi.testclient import TestClient
from src.api.app import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post(
    "/predict",
    json={
        "review": "This movie was amazing."
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "sentiment" in data
    assert "confidence" in data

