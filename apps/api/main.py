"""Entry point for the Bajki Generator FastAPI service."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .routes import stories_router
from .schemas import HealthResponse

APP_VERSION = "0.1.0"
settings = get_settings()


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""

    app = FastAPI(title="Bajki Generator API", version=APP_VERSION)

    cors_origins = sorted(
        set(
            ["http://127.0.0.1:5173", "http://localhost:5173"]
            + list(settings.frontend_origin)
        )
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
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
