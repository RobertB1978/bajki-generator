from urllib.parse import urljoin

import pytest
import requests


def test_story_endpoint_openapi():
    """Smoke test ensuring the stories endpoint is published."""

    base = "http://127.0.0.1:8000"
    try:
        response = requests.get(urljoin(base, "/openapi.json"), timeout=2)
    except requests.RequestException:
        pytest.skip("API server not reachable; skipping OpenAPI smoke test")

    assert "/api/stories" in response.text
