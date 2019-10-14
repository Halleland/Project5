import time


class LEDboard:
    def __init__(self):
        self.twinkle_time = .3  # time in seconds to sleep between twinkle


    def light_led(self, led_number):
        '''- Turn on one of the 6 LEDs by making the appropriate combination of input and
        output declarations, and then making the appropriate HIGH / LOW settings on the output
        pins.'''
        print("Lys på led; ", led_number)



    def setup(self):
        ''' Set the proper mode via: GPIO.setmode(GPIO.BCM).'''
        pass

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
        print("LEDs, skrudd av")

    def power_up(self):
        '''Power LED for start up sequence'''
        self.twinkle_all_leds(3)

    def shut_down(self):
        '''Power LED for shut down sequence'''
        self.twinkle_all_leds(3)
