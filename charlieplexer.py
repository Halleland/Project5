import RPi.GPIO as GPIO
import time


class LEDboard:
    def __init__(self):
        self.pins = -1
        self.pin_led_states = -1
        self.twinkle_time = .3  # time in seconds to sleep between twinkle

    def set_pin(self, pin_index, pin_state):
        '''Set pin at pin_index to pin_state'''
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_led(self, led_number):
        '''- Turn on one of the 6 LEDs by making the appropriate combination of input and
        output declarations, and then making the appropriate HIGH / LOW settings on the output
        pins.'''
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)

    def setup(self):
        ''' Set the proper mode via: GPIO.setmode(GPIO.BCM).'''
        self.pins = [5, 6, 13]

        self.pin_led_states = [
            [1, 0, -1],  # A
            [0, 1, -1],  # B
            [-1, 1, 0],  # C
            [-1, 0, 1],  # D
            [1, -1, 0],  # E
            [0, -1, 1]  # F
        ]

        GPIO.setmode(GPIO.BCM)
        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)

    def flash_all_leds(self, k):
        '''Flash all 6 LEDs on and off for k seconds'''
        current_time = time.time()
        seconds_passed = 0
        while seconds_passed < k:
            for i in range(0, 6):
                self.light_led(i)
            seconds_passed = time.time() - current_time
        self.turn_off_leds()

    def twinkle_all_leds(self, k):
        '''Turn all LEDs on and off in sequence for k seconds'''
        current_time = time.time()
        seconds_passed = 0
        while seconds_passed < k:
            for i in range(0, 6):
                self.light_led(i)
                time.sleep(self.twinkle_time)
            seconds_passed = time.time() - current_time
        self.turn_off_leds()

    def turn_off_leds(self):
        '''Turn off all LEDs'''
        for i in range(len(self.pins)):
            self.set_pin(i, -1)

    def power_up(self):
        '''Power LED for start up sequence'''
        self.twinkle_all_leds(3)

    def shut_down(self):
        '''Power LED for shut down sequence'''
        self.twinkle_all_leds(3)
