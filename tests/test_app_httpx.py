import pytest
from httpx import AsyncClient

base_url = "http://localhost:8181"


@pytest.mark.asyncio
async def test_health_endpoint_status_code():
    """
    Verify that the /health endpoint returns HTTP 200 OK status.

    This confirms that the service is up and responding.
    """
    async with AsyncClient(base_url=base_url) as client:
        response = await client.get("/health")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_endpoint_response_body():
    """
    Verify that the /health endpoint returns the expected JSON body.

    Checks that the JSON response contains:
    - 'status' key with value 'ok'
    - 'service' key with value 'Docker-GitHub-Action API'
    - 'uptime' key with a string value representing uptime duration
    """
    async with AsyncClient(base_url=base_url) as client:
        response = await client.get("/health")
        data = response.json()

        assert "status" in data
        assert "service" in data
        assert "uptime" in data

        assert data["status"] == "ok"
        assert data["service"] == "Docker-GitHub-Action API"
        assert isinstance(data["uptime"], str)


if __name__ == "__main__":
    """
    Async tests for the /health endpoint of the running FastAPI application.

    These tests use AsyncClient from HTTPX to make requests to the server
    running at http://localhost:8181. Make sure the server is running before
    executing these tests.
    """
    pytest.main()
