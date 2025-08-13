from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI, status

app = FastAPI(
    title="Docker-GitHub-Action Project",
    description="A sample FastAPI application demonstrating Docker deployment and GitHub Actions CI/CD pipeline.",
    version="1.0.0",
)

# Store app start time
app_start_time = datetime.utcnow()


def get_uptime() -> str:
    uptime_duration: timedelta = datetime.utcnow() - app_start_time
    days = uptime_duration.days
    hours, remainder = divmod(uptime_duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"


@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health Check Endpoint",
    description="Returns the health status and basic metadata of the service.",
)
async def get_health_status():
    """
    Health Check Endpoint
    Returns the current health status of the application with dynamic uptime.
    :return: Dictionary containing health status, service name, and uptime.
    """
    return {
        "status": "ok",
        "service": "Docker-GitHub-Action API",
        "uptime": get_uptime(),
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8181, reload=True)
