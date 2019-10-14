import time


class KPCAgent:

    def __init__(self, keypad, LED_board, password_file_path):
        self.keypad = keypad
        self.LED_board = LED_board
        self.passcode_buffer = []
        self.time_buffer = []
        self.password_file_path = password_file_path
        self.Lid = 0
        self.Ldur = 0
        self.override = 0
        self.previous_signal = 0

    def init_passcode_entry(self):
        """ - Clear the passcode-buffer and initiate a ”power up” lighting sequence
        on the LED Board. This should be done when the user first presses the keypad."""
        self.reset_password_accumulator()

    def fully_activate_agent(self):
        self.reset_password_accumulator()

    def reset_password_accumulator(self):
        self.passcode_buffer = []
        self.twinkle_leds()

    def get_next_signal(self):
        """ - Return the override-signal, if it is non-blank; otherwise query the keypad
        for the next pressed key."""
        if self.override != 0:
            temp = self.override
            self.override = 0
            return temp
        signal = self.keypad.get_next_signal()
        self.previous_signal = signal
        return signal

    def append_next_password_digit(self):
        self.passcode_buffer.append(self.previous_signal)

    def append_next_time_digit(self):
        self.time_buffer.append(self.previous_signal)

    def verify_password(self):
        self.verify_login()

    def verify_login(self):
        """ - Check that the password just entered via the keypad
        matches that in the password file. Store the result (Y or N)
        in the override-signal. Also, this should call the LED
        Board to initiate the appropriate lighting pattern for
        login success or failure."""
        password_file = open(self.password_file_path, "r")
        password = password_file.readline().strip()
        password_file.close()
        print("The password {} was read from file path {}"
              .format(password, self.password_file_path))
        if password == "".join(str(d) for d in self.passcode_buffer):
            print("You entered the right password!")
            self.override = "Y"
        else:
            print(str(password) + " does not match passcode buffer " + str(self.passcode_buffer))
            self.override = "N"
            self.flash_leds()

    def validate_password(self):
        if self.validate_passcode_change():
            self.twinkle_leds()
        else:
            self.flash_leds()

    def validate_passcode_change(self):
        """ - Check that the new password is legal. If so,
        write the new password in the password file. A legal
        password should be at least 4 digits long and should
        contain no symbols other than the digits 0-9. As in
        verify login, this should use the LED Board to signal
        success or failure in changing the password.2"""

        if len(self.passcode_buffer) < 4:
            # signal failure
            print("Password to short {}".format(self.passcode_buffer))
            self.reset_password_accumulator()
            return False
        if not all(is_digit, self.passcode_buffer):
            # signal failure
            print("Password must only contain digits {}".format(self.passcode_buffer))
            self.reset_password_accumulator()
            return False
        password_file = open(self.password_file_path, "w")
        password_file.write("".join(str(d) for d in self.passcode_buffer))
        password_file.truncate()
        password_file.close()
        self.reset_password_accumulator()
        return True

    def set_Lid(self):
        self.Lid = int(self.previous_signal)

    def reset_agent(self):
        print("What does reset_agent entail?")
        self.reset_password_accumulator()
        self.Lid = 0
        self.Ldur = 0
        self.override = 0
        self.time_buffer = []

    def light_one_led(self):
        """ - Using values stored in the Lid and Ldur slots, call the LED Board and request
        that LED # Lid be turned on for Ldur seconds."""
        self.Ldur = int("".join(str(d) for d in self.time_buffer))
        print("lighting LED {} for {} time".format(self.Lid, self.Ldur))
        self.LED_board.light_led(self.Lid)
        time.sleep(self.Ldur)
        self.LED_board.turn_off_leds()
        self.time_buffer = []

    def flash_leds(self):
        # - Call the LED Board and request the flashing of all LEDs.
        self.LED_board.flash_all_leds(2)

    def twinkle_leds(self):
        # - Call the LED Board and request the twinkling of all LEDs.
        self.LED_board.twinkle_all_leds(2)

    def exit_action(self):
        # - Call the LED Board to initiate the ”power down” lighting sequence.
        self.flash_leds()


def is_digit(d):
    return str(d).isdigit()


def all(p, l):
    def f(acc, x):
        acc = True
        if not p(x):
            acc = False
        return acc

    return reduce(f, l)


def reduce(f, l, acc=0):
    for i in range(len(l)):
        acc = f(acc, l[i])
    return acc
