"""Definerer Keypad-objektet som skal polle for input og videresende det til Agent-objektet."""
import RPi.GPIO as GPIO


class Keypad:
    """Implementasjon av Keypad-klassen."""

    def __init__(self):
        """Gjør nødvendig set-up."""
        GPIO.setmode(GPIO.BCM)
        for row_pins in [18, 23, 24, 25]:
            GPIO.setup(row_pins, GPIO.OUT)
        for column_pins in [17, 27, 22]:
            GPIO.setup(column_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
