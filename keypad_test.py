"""Inneholder test-versjonen av keypad-objektet."""


class Keypad:
    """Implementasjon av test-klassen Keypad."""

    def setup(self):
        """Kun for å hindre undef-error."""
        return

    def do_polling(self):
        """Returnerer input fra tastaturet."""
        return input()

    def get_next_signal(self):
        """Kun for å hindre undef-error."""
        return self.do_polling()
