"""Very small subset of :mod:`fastapi.testclient`."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import datetime
from enum import Enum
from typing import Any
import json

from .app import FastAPI


def _serialise(value: Any) -> Any:
    """Convert values returned by endpoints into JSON serialisable objects."""

    if is_dataclass(value):
        return {key: _serialise(sub_value) for key, sub_value in asdict(value).items()}

    if isinstance(value, dict):
        return {key: _serialise(sub_value) for key, sub_value in value.items()}

    if isinstance(value, (list, tuple, set, frozenset)):
        return [_serialise(item) for item in value]

    if isinstance(value, datetime):
        return value.isoformat()

    if isinstance(value, Enum):
        return value.value

    return value


class _Response:
    """Simple structure mimicking ``requests.Response`` in tests."""

    def __init__(self, status_code: int, payload: Any):
        self.status_code = status_code
        self._payload = _serialise(payload)

    def json(self) -> Any:
        return self._payload

    @property
    def text(self) -> str:
        if isinstance(self._payload, (dict, list)):
            return json.dumps(self._payload)
        return str(self._payload)


class TestClient:
    """Extremely small stand-in for FastAPI's TestClient."""

    __test__ = False  # Prevent pytest from treating this class as a test case.

    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path: str, **_: Any) -> _Response:
        status, payload = self.app.handle_request("GET", path)
        return _Response(status, payload)

    def post(self, path: str, json: Any = None, **_: Any) -> _Response:
        status, payload = self.app.handle_request("POST", path, body=json)
        return _Response(status, payload)

    def request(self, method: str, path: str, json: Any = None, **_: Any) -> _Response:
        status, payload = self.app.handle_request(method, path, body=json)
        return _Response(status, payload)
