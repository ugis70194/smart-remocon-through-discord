from remocon.messenger.dark import dark
from remocon.messenger.reset import reset
from remocon.messenger.warm import warm


def test_reset():
    assert 204 == reset()


def test_dark():
    assert 204 == dark()


def test_warm():
    assert 204 == warm()
