import json

from api import health


def test_health_handler_ok():
    status, headers, body = health.handler({"method": "GET"})
    assert status == 200
    data = json.loads(body)
    assert data["status"] == "ok"
