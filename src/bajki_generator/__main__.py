"""Pozwala uruchomić generator bajek poleceniem ``python -m bajki_generator``."""

from .cli import main


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
