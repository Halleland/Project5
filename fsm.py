"""Contains fsm class."""
from inspect import isfunction


def signal_is_digit(signal):
    """checks if signal is digit"""
    return ord('0') <= ord(signal) <= ord('9')


def signal_less_than_six(signal):
    """Check if signal is signal less than six"""
    if signal_is_digit(signal):
        return int(signal) < 6
    return False


def signal_is_symbol(signal):
    """Check if signal is symbol, eg string"""
    return isinstance(signal, str)


class Rule:
    def __init__(self):
        self.state1 = -1
        self.state2 = -1
        self.signal = -1
        self.action = -1


class Fsm:
    """
    Class for final state machine
    Should have the following states when implemented:
    S-init
    S-read
    S-verify
    S-active
    """

    def __init__(self, _agent):
        self.agent = _agent
        self.rule_list = []
        self.start_state = -1
        self.end_state = -1
        self.state = 0

    def set_start_state(self, state):
        self.start_state = state

    def set_end_state(self, state):
        self.end_state = state

    def addRule(self, state1, state2, signal, action):
        """Add a new rule to the rule list"""
        rule = Rule()
        rule.state1 = state1
        rule.state2 = state2
        rule.signal = signal
        rule.action = action
        self.rule_list.append(rule)

    def get_next_signal(self):
        """Query next singal from agent"""
        return self.agent.get_next_signal()

    def run_rules(self, signal):
        """Apply rules until one fires"""
        for rule in self.rule_list:
            if self.apply_rule(rule, signal):
                self.fire_rule(rule)
                break

    def apply_rule(self, rule, signal):
        """Check if condintions for rule are met"""
        b1 = rule.state1(signal) if isfunction(rule.state1) else rule.state1 == self.state
        b2 = rule.signal(signal) if isfunction(rule.signal) else rule.signal == signal
        return b1 and b2

    def fire_rule(self, rule):
        """Change state and perform action according to rule"""
        print(self.state, "->", rule.state2)
        self.state = rule.state2
        if rule.action is not None:
            rule.action()

    def main_loop(self):
        """Begin FSM in start state and repeatedly call for next
        signal and run rules until it enters final state"""
        self.state = self.start_state
        while self.state != self.end_state:
            signal = self.get_next_signal()
            self.run_rules(signal)


if __name__ == "__main__":
    agent = None
    sm = Fsm(agent)
