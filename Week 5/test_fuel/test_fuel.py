import fuel
import pytest

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/1") == 100

    with pytest.raises(ValueError):
        fuel.convert("5/4")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(50) == "50%"
