from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("2/3") == 67


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ValueError):
        convert("4/3")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("-7/4")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"