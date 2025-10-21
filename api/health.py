from __future__ import annotations
import json
from typing import Any


def handler(_request: dict[str, Any] | None = None):
    return (200, {"Content-Type": "application/json"}, json.dumps({"status": "ok"}))
