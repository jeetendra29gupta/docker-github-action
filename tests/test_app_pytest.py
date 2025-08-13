import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_endpoint_status_code():
    """
    Test that the /health endpoint returns a 200 OK status code.
    """
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_response_body():
    """
    Test that the /health endpoint returns the expected keys and values:
    - 'status': must be 'ok'
    - 'service': must be 'Docker-GitHub-Action API'
    - 'uptime': must be a string
    """
    response = client.get("/health")
    data = response.json()

    assert "status" in data
    assert "service" in data
    assert "uptime" in data

    assert data["status"] == "ok"
    assert data["service"] == "Docker-GitHub-Action API"
    assert isinstance(data["uptime"], str)


if __name__ == "__main__":
    """
    Test suite for the FastAPI application defined in main.py.

    This module uses FastAPI's TestClient and pytest to test the /health endpoint,
    verifying both the status code and structure of the response.
    """
    pytest.main()
