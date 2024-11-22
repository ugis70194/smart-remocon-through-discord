from remocon.messenger.airconCool import airconCool
from remocon.messenger.airconOff import airconOff
from remocon.messenger.airconWarm import airconWarm
from remocon.messenger.dark import dark
from remocon.messenger.reset import reset
from remocon.messenger.warm import warm


def test_reset():
    assert 204 == reset()


def test_dark():
    assert 204 == dark()


def test_warm():
    assert 204 == warm()


def test_airconOff():
    assert 204 == airconOff()


def test_airconCool():
    assert 204 == airconCool()


def test_airconWarm():
    assert 204 == airconWarm()
