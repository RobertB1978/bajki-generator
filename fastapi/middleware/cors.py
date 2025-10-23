"""No-op CORS middleware placeholder."""

from __future__ import annotations

from typing import Any, Iterable


class CORSMiddleware:
    """Record configuration for documentation purposes."""

    def __init__(
        self,
        app: Any = None,
        *,
        allow_origins: Iterable[str] | None = None,
        allow_credentials: bool = False,
        allow_methods: Iterable[str] | None = None,
        allow_headers: Iterable[str] | None = None,
    ) -> None:
        self.app = app
        self.allow_origins = list(allow_origins or [])
        self.allow_credentials = allow_credentials
        self.allow_methods = list(allow_methods or [])
        self.allow_headers = list(allow_headers or [])
