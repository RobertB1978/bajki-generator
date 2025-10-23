"""Lightweight FastAPI-compatible facade used in tests.

This module provides a tiny subset of the FastAPI public API sufficient for
unit tests.  It intentionally mirrors the real package's interface only where
necessary so the rest of the code base can remain unchanged while avoiding a
heavy dependency graph.
"""

from .app import APIRouter, Depends, FastAPI

__all__ = ["APIRouter", "Depends", "FastAPI"]
