import json

from api import stories


def test_story_handler_ok():
    status, headers, body = stories.handler({
        "method": "POST",
        "body": json.dumps({"hero": "Ala", "mood": "pogodny"})
    })
    assert status == 200
    data = json.loads(body)
    assert "title" in data and "story" in data
