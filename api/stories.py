from __future__ import annotations
import json
from typing import Any

ALLOWED_MOODS = {"pogodny", "zabawny", "tajemniczy", "przygodowy"}

def _bad_request(msg: str):
    return (
        400,
        {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        json.dumps({"error": msg})
    )

def handler(request: dict[str, Any]):
    method = str(request.get("method", "")).upper()
    if method == "OPTIONS":
        return (
            204,
            {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            ""
        )

    if method != "POST":
        return _bad_request("Use POST with JSON body")

    raw_body = request.get("body", "{}")
    try:
        payload = raw_body.decode() if isinstance(raw_body, (bytes, bytearray)) else raw_body
        data = json.loads(payload or "{}")
    except Exception:
        return _bad_request("Invalid JSON")

    hero = str(data.get("hero", "Bohater")).strip() or "Bohater"
    mood = str(data.get("mood", "pogodny")).strip()
    if mood and mood not in ALLOWED_MOODS:
        return _bad_request(f"Unsupported mood. Allowed: {sorted(ALLOWED_MOODS)}")

    # tu normalnie podpięlibyśmy model/LLM; na razie deterministyczny generator
    title = f"Przygoda {hero}"
    text = f"{hero} wyrusza w {mood or 'pogodny'} dzień, by odkryć mały sekret w lesie..."

    body = {
        "title": title,
        "hero": hero,
        "mood": mood or "pogodny",
        "story": [{"title": "Rozdział 1", "text": text}]
    }
    return (
        200,
        {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        json.dumps(body)
    )
