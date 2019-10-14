"""Inneholder test-versjonen av keypad-objektet."""


class Keypad:
    """Implementasjon av test-klassen Keypad."""

    def setup(self):
        """Kun for å hindre undef-error."""
        return

    def get_input(self):
        """Returnerer input fra tastaturet."""
        return input()
