import pytest
from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("2/3") < 100
    assert convert("3/3") == 100
    assert convert("5/10") == 50
    assert convert("0/6") < 1
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("3/2")


def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(20) == f"{20}%"
    assert gauge(98) == f"{98}%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
