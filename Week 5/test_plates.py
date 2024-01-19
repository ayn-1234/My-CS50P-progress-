from plates import is_valid


def test_all_letters():
    assert is_valid("HELLO") == True
    assert is_valid("CS") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_zero():
    assert is_valid("0000") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("0908") == False

def test_all_numbers():
    assert is_valid("4578") == False
    assert is_valid("0908") == False

def test_others():
    assert is_valid("PI3.14") == False
    assert is_valid("Hello, 03") == False
    assert is_valid("GOODBYE") == False

#Completed assingment
#Alhamdulliah
