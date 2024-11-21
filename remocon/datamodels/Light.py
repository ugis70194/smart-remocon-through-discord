from collections import deque
from enum import Enum

from ..utils.signal import send_signal


class State(Enum):
    OFF = 0
    night = 1
    ON = 2


class Light:
    def __init__(self):
        self.state: State = State.ON
        self.brightness: int = 10
        self.temperature: int = 3
        self.command_que: deque = deque()

    def on(self):
        if self.state == State.ON:
            pass
        elif self.state == State.night:
            send_signal("light:toggle")
            send_signal("light:toggle")
        elif self.state == State.OFF:
            send_signal("light:toggle")

        self.state = State.ON

        # que signal 解消
        while len(self.command_que) > 0:
            cmd = self.command_que.pop()
            send_signal(cmd)

    def off(self):
        if self.state == State.ON:
            send_signal("light:toggle")
            send_signal("light:toggle")
        elif self.state == State.night:
            send_signal("light:toggle")
        elif self.state == State.OFF:
            pass

        self.state = State.OFF

    def night(self):
        if self.state == State.ON:
            send_signal("light:toggle")
        elif self.state == State.night:
            pass
        elif self.state == State.OFF:
            send_signal("light:toggle")
            send_signal("light:toggle")

        self.state = State.night

    def toBright(self):
        if self.brightness >= 10:
            return
        if self.state == State.OFF or self.state == State.night:
            self.command_que.append("light:toBright")
        else:
            send_signal("light:toBright")

        self.brightness += 1

    def toDark(self):
        if self.brightness <= 1:
            return
        if self.state == State.OFF or self.state == State.night:
            self.command_que.append("light:toDark")
        else:
            send_signal("light:toDark")

        self.brightness -= 1

    def toWarm(self):
        if self.temperature >= 5:
            return
        if self.state == State.OFF or self.state == State.night:
            self.command_que.append("light:toWarm")
        else:
            send_signal("light:toWarm")

        self.temperature += 1

    def toCool(self):
        if self.temperature <= 1:
            return
        if self.state == State.OFF or self.state == State.night:
            self.command_que.append("light:toCool")
        else:
            send_signal("light:toCool")

        self.temperature -= 1

    def full(self):
        self.__init__()
        send_signal("light:full")

    def reset(self):
        self.__init__()

    def show(self):
        return (self.state, self.brightness, self.temperature, self.command_que)
