"""Tiny stub of the :mod:`requests` package used in tests."""

from __future__ import annotations


class RequestException(Exception):
    """Base exception for network errors."""


def get(*args, **kwargs):  # noqa: D401
    """Raise :class:`RequestException` to indicate networking is unavailable."""

    raise RequestException("HTTP access is not available in the test environment")
