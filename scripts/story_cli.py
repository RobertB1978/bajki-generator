#!/usr/bin/env python3
"""Command line helper for generating sample stories."""
from __future__ import annotations

import json

import httpx
import typer

API_URL = "http://localhost:8000/api/stories"

cli = typer.Typer(help="Generowanie bajek z wiersza poleceń")


@cli.command()
def generate(
    hero: str = typer.Argument(..., help="Imię bohatera"),
    age: int = typer.Option(5, help="Wiek słuchacza"),
    topic: str = typer.Option("kosmos", help="Motyw przewodni"),
    mood: str = typer.Option("pogodny", help="Nastrój historii"),
    length: str = typer.Option("short", help="Długość bajki: short, medium lub long"),
    api_url: str = typer.Option(API_URL, envvar="BAJKI_API_URL", help="Adres API"),
    pretty: bool = typer.Option(True, help="Czy formatować wynik"),
) -> None:
    """Generate a story using the running API."""

    payload = {
        "hero": hero,
        "age": age,
        "topic": topic,
        "mood": mood,
        "length": length,
    }
    response = httpx.post(api_url, json=payload, timeout=30)
    response.raise_for_status()

    content = response.json()
    if pretty:
        typer.echo(json.dumps(content, ensure_ascii=False, indent=2))
    else:
        typer.echo(response.text)


if __name__ == "__main__":
    cli()
