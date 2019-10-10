class KPCAgent:

	def __init__(self, keypad, LED_board, password_file_path):
		self.keypad = keypad
		self.LED_board = LED_board
		self.passcode_buffer = []
		self.password_file_path = password_file_path
		self.Lid = 0
		self.Ldur = 0
		self.override = 0

	def init_passcode_entry(self):
		""" - Clear the passcode-buffer and initiate a ”power up” lighting sequence
		on the LED Board. This should be done when the user first presses the keypad."""
		self.passcode_buffer = []

		pass

	def get_next_signal(self):
		""" - Return the override-signal, if it is non-blank; otherwise query the keypad
		for the next pressed key."""
		if self.override != 0:
			return self.override
		return self.keypad.get_next_signal()

	def verify_login(self):
		""" - Check that the password just entered via the keypad 
		matches that in the password file. Store the result (Y or N) 
		in the override-signal. Also, this should call the LED
		Board to initiate the appropriate lighting pattern for 
		login success or failure."""
		password_file = open(self.password_file_path)
		password = password_file.read().strip()
		print("The password {} was read from file path {}"
			.format(password, self.password_file_path))
		if password == "".join(str(d) for d in self.passcode_buffer):
			print("You entered the right password!")
			self.override = "Y"
		else:
			print(str(password) + " does not match passcode buffer " + str(self.passcode_buffer))
			self.override = "N"

	def validate_passcode_change(self):
		""" - Check that the new password is legal. If so, 
		write the new password in the password file. A legal 
		password should be at least 4 digits long and should
		contain no symbols other than the digits 0-9. As in 
		verify login, this should use the LED Board to signal 
		success or failure in changing the password.2"""
		
		if len(self.passcode_buffer) < 4:
			#signal failure
			print("Password to short {}".format(self.passcode_buffer))
			return
		if not "".join(str(d) for d in self.passcode_buffer).isdigit():
			#signal failure
			print("Password must only contain digits {}".format(self.passcode_buffer))
			return 



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

def is_digit(d):
	return str(d).isdigit()

def all(p, l):
	def f(acc, x):
		acc = True
		if not p(x):
			acc = False
		return acc
	return reduce(f, l)

def reduce(f, l, acc = 0):
	for i in range(len(l)):
		acc = f(acc, l[i])
	return acc
