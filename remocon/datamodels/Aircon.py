from enum import Enum

from ..utils.signal import send_signal


class State(Enum):
    OFF = 0
    COOL = 1
    WARM = 2


class Aircon:
    def __init__(self):
        self.state = State.OFF
        self.temperature = 25

    def off(self):
        self.state = State.OFF
        send_signal("aircon:off")

    def cool(self):
        self.state = State.COOL
        self.temperature = 26
        send_signal("aircon:cool_26")

    def warm(self):
        self.state = State.WARM
        self.temperature = 21
        send_signal("aircon:warm_21")

    def tempUp_cool(self):
        self.temperature = min(30, self.temperature + 1)
        send_signal(f"aircon:cool_{self.temperature}")

    def tempDown_cool(self):
        self.temperature = max(18, self.temperature - 1)
        send_signal(f"aircon:cool_{self.temperature}")

    def tempUp_warm(self):
        self.temperature = min(27, self.temperature + 1)
        send_signal(f"aircon:warm_{self.temperature}")

    def tempDown_warm(self):
        self.temperature = max(18, self.temperature - 1)
        send_signal(f"aircon:warm_{self.temperature}")

    def show(self):
        return (self.state, self.temperature)
