"""Vercel serverless entry point for the FastAPI application."""

from apps.api.main import app as fastapi_app

app = fastapi_app
