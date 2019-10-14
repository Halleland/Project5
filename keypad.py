"""Definerer Keypad-objektet som skal polle for input og videresende det til Agent-objektet."""
import time
import RPi.GPIO as GPIO


class Keypad:
    """Implementasjon av Keypad-klassen."""

    def __init__(self):
        """Definerer rad- og kolonne-pins, og oppretter dict. for key-mapping."""
        self.row_pins = [18, 23, 24, 25]
        self.column_pins = [17, 27, 22]
        self.keys = {(self.row_pins[0], self.column_pins[0]): '1',
                     (self.row_pins[0], self.column_pins[1]): '2',
                     (self.row_pins[0], self.column_pins[2]): '3',
                     (self.row_pins[1], self.column_pins[0]): '4',
                     (self.row_pins[1], self.column_pins[1]): '5',
                     (self.row_pins[1], self.column_pins[2]): '6',
                     (self.row_pins[2], self.column_pins[0]): '7',
                     (self.row_pins[2], self.column_pins[1]): '8',
                     (self.row_pins[2], self.column_pins[2]): '9',
                     (self.row_pins[3], self.column_pins[0]): '*',
                     (self.row_pins[3], self.column_pins[1]): '0',
                     (self.row_pins[3], self.column_pins[2]): '#'}

    def setup(self):
        """Gjør nødvendig set-up."""
        GPIO.setmode(GPIO.BCM)
        for pins in self.row_pins:
            GPIO.setup(pins, GPIO.OUT)
        for pins in self.column_pins:
            GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_input(self):
        """Poller for input og returnerer en string av key pressed."""
        for rows in self.row_pins:
            GPIO.output(rows, GPIO.HIGH)
            for columns in self.column_pins:
                i = 1
                while GPIO.input(columns) == GPIO.HIGH:
                    i += 1
                    time.sleep(0.01)
                    if i >= 20:
                        return self.keys.get((rows, columns))
            GPIO.output(rows, GPIO.LOW)
