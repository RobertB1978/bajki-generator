"""Middleware facade exposing only the features we need."""

from .cors import CORSMiddleware

__all__ = ["CORSMiddleware"]
