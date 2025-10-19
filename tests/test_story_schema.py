"""Smoke checks for the story endpoint definition."""

from urllib.parse import urljoin

import pytest
import requests


@pytest.mark.integration
def test_story_endpoint_openapi():
    """Ensure the `/api/stories` endpoint is present in the OpenAPI schema."""

    base = "http://127.0.0.1:8000"
    try:
        response = requests.get(urljoin(base, "/openapi.json"), timeout=2)
    except requests.RequestException as exc:  # pragma: no cover - network dependent
        pytest.skip(f"OpenAPI schema not reachable: {exc}")

    assert "/api/stories" in response.text
