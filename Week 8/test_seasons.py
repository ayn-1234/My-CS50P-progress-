from seasons import check_date
from seasons import count_minutes
import pytest

def test_seasons():
    with pytest.raises(ValueError):
        check_date("January 9, 2023")

    assert count_minutes(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert count_minutes(730) == "One million, fifty-one thousand, two hundred minutes"
