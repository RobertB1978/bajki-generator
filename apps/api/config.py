"""Application settings and configuration helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
import os
from typing import List


def _split_csv(value: str) -> List[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(slots=True)
class Settings:
    """Strongly typed runtime configuration without external dependencies."""

    api_prefix: str = "/api"
    frontend_origin: List[str] = field(
        default_factory=lambda: [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ]
    )
    default_language: str = "pl"

    @classmethod
    def from_environment(cls) -> "Settings":
        """Build settings using ``BAJKI_`` prefixed environment variables."""

        data: dict[str, object] = {}
        prefix = "BAJKI_"

        api_prefix = os.getenv(f"{prefix}API_PREFIX")
        if api_prefix:
            data["api_prefix"] = api_prefix.strip()

        frontend_origin = os.getenv(f"{prefix}FRONTEND_ORIGIN")
        if frontend_origin:
            data["frontend_origin"] = _split_csv(frontend_origin)

        default_language = os.getenv(f"{prefix}DEFAULT_LANGUAGE")
        if default_language:
            data["default_language"] = default_language.strip()

        return cls(**data)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached instance of :class:`Settings`."""

    return Settings.from_environment()
