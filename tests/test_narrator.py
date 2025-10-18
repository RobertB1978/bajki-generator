from __future__ import annotations

from pathlib import Path

from bajki_generator.narrator import NarrationError, SimpleNarrator


def test_narrator_creates_wave_file(tmp_path: Path) -> None:
    narrator = SimpleNarrator(sample_rate=8000, symbol_duration=0.05, silence_duration=0.02)
    output = tmp_path / "narracja.wav"
    narrator.synthesize_to_file("To jest próba.", output)

    assert output.exists()
    assert output.stat().st_size > 0


def test_narrator_rejects_empty_text(tmp_path: Path) -> None:
    narrator = SimpleNarrator()
    with pytest.raises(NarrationError):  # type: ignore[name-defined]
        narrator.synthesize_to_file("   \n\t", tmp_path / "plik.wav")


import pytest  # noqa: E402  pylint: disable=wrong-import-position
