from working import convert
import pytest


def test_with_minutes():
    assert convert("9:42 AM to 5 PM") == "09:42 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_without_minutes():
    assert convert("12 PM to 9:42 AM") == "12:00 to 09:42"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
#Completed assingment
#Alhamdulliah
