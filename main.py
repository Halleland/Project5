import FSM as fsm
import KPCAgent
import charlieplexer as led
import keypad
import led_test
import keypad_test


def run():
    password_path = "./pass.txt"
    pad = keypad.Keypad()
    #testpad = keypad_test.Keypad()
    ledboard = led.LEDboard()
    #testledboard = led_test.LEDboard()
    ledboard.setup()
    kpc = KPCAgent.KPCAgent(pad, ledboard, password_path)
    #kpc = KPCAgent.KPCAgent(testpad, testledboard, password_path)
    
    thefsm = fsm.Fsm(kpc)
    # Add fsm rules
    thefsm.addRule("S-init", "S-read", fsm.signal_is_symbol, kpc.reset_password_accumulator)
    thefsm.addRule("S-read", "S-read", fsm.signal_is_digit, kpc.append_next_password_digit)
    thefsm.addRule("S-read", "S-verify", "*", kpc.verify_password)
    thefsm.addRule("S-read", "S-init", fsm.signal_is_symbol, kpc.reset_agent)
    thefsm.addRule("S-verify", "S-active", "Y", kpc.fully_activate_agent)
    thefsm.addRule("S-verify", "S-init", fsm.signal_is_symbol, kpc.reset_agent)
    thefsm.addRule("S-active", "S-led", fsm.signal_less_than_six, kpc.set_Lid)  # sett led
    thefsm.addRule("S-active", "S-password", "*", None)  # Begynn passordendring
    thefsm.addRule("S-active", "S-logout", "#", None)
    thefsm.addRule("S-led", "S-time", "*", None)  # Begynn Sett tid, kanskje None
    thefsm.addRule("S-time", "S-time", fsm.signal_is_digit, kpc.append_next_time_digit)  # Legg til på tid
    thefsm.addRule("S-time", "S-active", "*", kpc.light_one_led)
    thefsm.addRule("S-password", "S-password", fsm.signal_is_digit,
                   kpc.append_next_password_digit)  # Legg til på endret passord
    thefsm.addRule("S-password", "S-active", "*", kpc.validate_password)
    thefsm.addRule("S-logout", "S-done", "#", kpc.exit_action)
    thefsm.addRule("S-logout", "S-active", fsm.signal_is_symbol, None)
    thefsm.addRule("S-done", "S-read", fsm.signal_is_symbol, kpc.reset_agent())

    thefsm.set_start_state("S-init")
    # fsm.set_end_state("S-end")#Har ingen end state foreløpig
    thefsm.main_loop()


if __name__ == "__main__": run()
