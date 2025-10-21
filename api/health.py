"""Health check endpoint for the Vercel deployment."""

from __future__ import annotations

from importlib.metadata import version

from fastapi import FastAPI

from apps.api.schemas import HealthResponse

app = FastAPI(title="Bajki Generator API - Health")


@app.get("/")
def healthcheck() -> HealthResponse:  # pragma: no cover - exercised in deployment
    """Return a lightweight health response for uptime monitoring."""

    return HealthResponse(status="ok", version=version("fastapi"))
