class KPCAgent:

	def __init__(self, keypad, LED_board, password_file):
		self.keypad = keypad
		self.LED_board = LED_board
		self.passcode_buffer = []
		self.password_file = password_file
		self.Lid = 0
		self.Ldur = 0

	def init_passcode_entry(self):
		""" - Clear the passcode-buffer and initiate a ”power up” lighting sequence
		on the LED Board. This should be done when the user first presses the keypad."""
		pass

	def get_next_signal(self):
		""" - Return the override-signal, if it is non-blank; otherwise query the keypad
		for the next pressed key."""
		pass

	def verify_login(self):
		""" - Check that the password just entered via the keypad matches that in the password file. Store the result (Y or N) in the override-signal. Also, this should call the LED
		Board to initiate the appropriate lighting pattern for login success or failure."""
		pass

	def validate_passcode_change(self):
		""" - Check that the new password is legal. If so, write the new password in the password file. A legal password should be at least 4 digits long and should
		contain no symbols other than the digits 0-9. As in verify login, this should use the LED
		Board to signal success or failure in changing the password.2"""
		pass


	def light_one_led(self):
		""" - Using values stored in the Lid and Ldur slots, call the LED Board and request
		that LED # Lid be turned on for Ldur seconds."""
		pass

	def flash_leds(self):
		# - Call the LED Board and request the flashing of all LEDs.
		pass

	def twinkle_leds(self):
		# - Call the LED Board and request the twinkling of all LEDs.
		pass

	def exit_action(self):
		# - Call the LED Board to initiate the ”power down” lighting sequence.
		pass