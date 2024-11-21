from collections import deque

from remocon.datamodels.Light import Light, State

light = Light()


def test_init():
    light.__init__()
    assert light.show() == (State.ON, 10, 3, deque([]))


def test_off():
    light.__init__()
    light.off()
    assert light.show() == (State.OFF, 10, 3, deque([]))


def test_on():
    light.__init__()
    light.state = State.OFF
    light.on()
    assert light.show() == (State.ON, 10, 3, deque([]))


def test_night():
    light.__init__()
    light.state = State.OFF
    light.night()
    assert light.show() == (State.night, 10, 3, deque([]))


def test_toDark():
    light.__init__()
    light.toDark()
    assert light.show() == (State.ON, 9, 3, deque([]))


def test_toBright():
    light.__init__()
    light.brightness = 5
    light.toBright()
    assert light.show() == (State.ON, 6, 3, deque([]))


def test_toWarm():
    light.__init__()
    light.toWarm()
    assert light.show() == (State.ON, 10, 4, deque([]))


def test_toCool():
    light.__init__()
    light.toCool()
    assert light.show() == (State.ON, 10, 2, deque([]))


def test_full():
    light.__init__()
    light.state = State.OFF
    light.brightness = 1
    light.temperature = 1
    light.full()
    assert light.show() == (State.ON, 10, 3, deque([]))


def test_stackToDark():
    light.__init__()
    light.state = State.OFF
    light.toDark()
    assert light.show() == (State.OFF, 9, 3, deque(["light:toDark"]))


def test_stackToBright():
    light.__init__()
    light.state = State.OFF
    light.brightness = 8
    light.toBright()
    assert light.show() == (State.OFF, 9, 3, deque(["light:toBright"]))


def test_stackToWarm():
    light.__init__()
    light.state = State.OFF
    light.toWarm()
    assert light.show() == (State.OFF, 10, 4, deque(["light:toWarm"]))


def test_stackToDark():
    light.__init__()
    light.state = State.OFF
    light.toCool()
    assert light.show() == (State.OFF, 10, 2, deque(["light:toCool"]))
