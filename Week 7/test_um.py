from um import count


def test_valid():
    assert count("um,") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1


def test_invalid():
    assert count("Yum, Yummy") == 0
    assert count("Sum, Summing up") == 0
    assert count("Umm") == 0


def test_others():
    assert count("Um, thanks, um...,") == 2
    assert count("Um, Excuse me, Um... Hello??") == 2
