from working import convert
import pytest


def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_midnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_noon():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_same_time():
    assert convert("1 PM to 1 PM") == "13:00 to 13:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_missing_period():
    with pytest.raises(ValueError):
        convert("9 to 5 PM")


def test_invalid_period():
    with pytest.raises(ValueError):
        convert("9 XM to 5 PM")


def test_letters():
    with pytest.raises(ValueError):
        convert("nine AM to five PM")