"""Prosty syntetyzator audio tworzący pliki WAV na podstawie tekstu."""

from __future__ import annotations

from array import array
from pathlib import Path
import math
import wave


class NarrationError(RuntimeError):
    """Błąd zgłaszany, gdy nie uda się wygenerować narracji."""


class SimpleNarrator:
    """Minimalistyczny narrator tworzący prosty plik WAV.

    Zamiast prawdziwej syntezy mowy narrator tworzy muzyczną reprezentację
    tekstu: dla każdego znaku generowany jest krótki ton o unikalnej częstotliwości,
    a odstępy między słowami odwzorowane są ciszą. Dzięki temu nawet w środowisku
    bez zewnętrznych bibliotek TTS użytkownik otrzymuje dźwiękowy plik, który może
    posłużyć jako placeholder narracji.
    """

    def __init__(
        self,
        sample_rate: int = 22_050,
        symbol_duration: float = 0.18,
        silence_duration: float = 0.08,
        amplitude: int = 10_000,
    ) -> None:
        if sample_rate <= 0:
            raise ValueError("Częstotliwość próbkowania musi być dodatnia.")
        if symbol_duration <= 0:
            raise ValueError("Czas trwania dźwięku dla znaku musi być dodatni.")
        if silence_duration < 0:
            raise ValueError("Czas ciszy nie może być ujemny.")
        if not 0 < amplitude <= 32_767:
            raise ValueError("Amplituda musi mieścić się w zakresie (0, 32767].")

        self.sample_rate = sample_rate
        self.symbol_duration = symbol_duration
        self.silence_duration = silence_duration
        self.amplitude = amplitude

    def synthesize_to_file(self, text: str, output_path: Path | str) -> Path:
        """Generuje plik WAV z prostą narracją."""

        if not text or not text.strip():
            raise NarrationError("Tekst do syntezy nie może być pusty.")

        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)

        frames = self._render_text(text)
        if not frames:
            raise NarrationError("Nie wygenerowano żadnych danych audio.")

        try:
            with wave.open(str(destination), "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(self.sample_rate)
                wav_file.writeframes(frames.tobytes())
        except OSError as exc:  # pragma: no cover - zależne od systemu plików
            raise NarrationError("Nie udało się zapisać pliku WAV") from exc

        return destination

    # region internals
    def _render_text(self, text: str) -> array:
        frames = array("h")
        for index, char in enumerate(text):
            if char.isspace():
                frames.extend(self._silence())
                if char == "\n" and (index + 1) < len(text):
                    frames.extend(self._silence())
                continue
            frequency = self._frequency_for_character(char)
            frames.extend(self._tone(frequency))
        frames.extend(self._silence())
        return frames

    def _tone(self, frequency: float) -> array:
        total_samples = max(1, int(self.sample_rate * self.symbol_duration))
        wave_points = array("h")
        two_pi = 2 * math.pi
        for i in range(total_samples):
            phase = two_pi * frequency * (i / self.sample_rate)
            value = int(self.amplitude * math.sin(phase))
            wave_points.append(value)
        return wave_points

    def _silence(self) -> array:
        silent_samples = int(self.sample_rate * self.silence_duration)
        return array("h", [0] * silent_samples)

    def _frequency_for_character(self, char: str) -> float:
        base = 220.0
        spread = 220.0
        code = ord(char)
        return base + (code % int(spread))

    # endregion


__all__ = ["SimpleNarrator", "NarrationError"]
