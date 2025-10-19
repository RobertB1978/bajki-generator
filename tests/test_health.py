from fastapi.testclient import TestClient
from apps.api.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") in ("ok", "healthy", "OK", "HEALTHY")
