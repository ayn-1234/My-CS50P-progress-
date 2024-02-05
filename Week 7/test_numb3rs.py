from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.1.2.3") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2343.3555.1000") == False
    assert validate("cat") == False

#Completed assingments
#Alhamdulliah
