from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"name": "Digital Routine Generator"}


def test_read_health_check():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# pip install pytest pytest-asyncio httpx anyio
# pytest