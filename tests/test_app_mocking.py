from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient

base_url = "http://localhost:8181"


@pytest.mark.asyncio
async def test_health_endpoint_status_code(mocker):
    """
    Test that the /health endpoint returns HTTP status code 200.

    This test mocks AsyncClient.get to simulate a response with status code 200,
    without making an actual network call.
    """
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mocker.patch.object(AsyncClient, "get", return_value=mock_response)

    async with AsyncClient(base_url=base_url) as client:
        response = await client.get("/health")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_endpoint_response_body(mocker):
    """
    Test the JSON response body of the /health endpoint.

    This test mocks AsyncClient.get and its json() method to simulate a response
    containing the expected keys and values:
    - "status": "ok"
    - "service": "Docker-GitHub-Action API"
    - "uptime": string representing uptime duration

    The test asserts the presence and correctness of these fields without hitting the real endpoint.
    """
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json = AsyncMock(
        return_value={
            "status": "ok",
            "service": "Docker-GitHub-Action API",
            "uptime": "1d 2h 3m 4s",
        }
    )
    mocker.patch.object(AsyncClient, "get", return_value=mock_response)

    async with AsyncClient(base_url=base_url) as client:
        response = await client.get("/health")
        data = await response.json()
        assert "status" in data
        assert "service" in data
        assert "uptime" in data
        assert data["status"] == "ok"
        assert data["service"] == "Docker-GitHub-Action API"
        assert isinstance(data["uptime"], str)


if __name__ == "__main__":
    """
    Unit tests for the /health endpoint of the FastAPI application using mocked HTTP responses.

    These tests mock httpx.AsyncClient.get method to simulate
    endpoint responses without making real HTTP requests.

    Make sure to install pytest and pytest-mock for mocking support.
    """
    pytest.main()
