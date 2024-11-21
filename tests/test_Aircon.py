from remocon.datamodels.Aircon import Aircon, State

aircon = Aircon()


def test_init():
    aircon.__init__()
    assert aircon.show() == (State.OFF, 25)


def test_off():
    aircon.__init__()
    aircon.state = State.COOL
    aircon.off()
    assert aircon.show() == (State.OFF, 25)


def test_cool():
    aircon.__init__()
    aircon.cool()
    assert aircon.show() == (State.COOL, 26)


def test_warm():
    aircon.__init__()
    aircon.warm()
    assert aircon.show() == (State.WARM, 21)


def test_tempUp_cool():
    aircon.__init__()
    aircon.cool()
    aircon.tempUp_cool()
    assert aircon.show() == (State.COOL, 27)


def test_tempDown_cool():
    aircon.__init__()
    aircon.cool()
    aircon.tempDown_cool()
    assert aircon.show() == (State.COOL, 25)


def test_tempUp_warm():
    aircon.__init__()
    aircon.warm()
    aircon.tempUp_warm()
    assert aircon.show() == (State.WARM, 22)


def test_tempDown_warm():
    aircon.__init__()
    aircon.warm()
    aircon.tempDown_warm()
    assert aircon.show() == (State.WARM, 20)
