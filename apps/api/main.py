"""Entry point for the Bajki Generator FastAPI service."""
from __future__ import annotations

from importlib.metadata import version

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .routes import stories_router
from .schemas import HealthResponse

settings = get_settings()


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""

    app = FastAPI(title="Bajki Generator API", version=version("fastapi"))

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.frontend_origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", response_model=HealthResponse, tags=["health"])
    def healthcheck() -> HealthResponse:  # pragma: no cover - trivial
        return HealthResponse(status="ok", version=app.version)

    app.include_router(stories_router, prefix=settings.api_prefix)
    return app


app = create_app()
