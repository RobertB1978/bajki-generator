"""Application settings and configuration helpers."""

from __future__ import annotations

from functools import lru_cache
from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Strongly typed runtime configuration."""

    api_prefix: str = Field("/api", description="Prefix for REST endpoints")
    frontend_origin: List[str] = Field(
        default_factory=lambda: ["http://localhost:5173", "http://127.0.0.1:5173"],
        description="Allowed CORS origins for the frontend application.",
    )
    default_language: str = Field(
        "pl", description="Default language for generated stories"
    )

    model_config = {
        "env_file": ".env",
        "env_prefix": "BAJKI_",
    }

    @field_validator("frontend_origin", mode="before")
    @classmethod
    def _ensure_list(cls, value: str | List[str]) -> List[str]:  # noqa: D401
        """Allow passing a comma separated list via the environment."""

        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached instance of :class:`Settings`."""

    return Settings()
