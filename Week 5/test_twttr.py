from twttr import shorten

def test_capital():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Stan") == "Stn"
    assert shorten("Harvard") == "Hrvrd"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("stan") == "stn"
    assert shorten("harvard") == "hrvrd"
    assert shorten("1") == "1"

#completed assingment
#Alhamdulliah

