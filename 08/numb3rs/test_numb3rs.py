from numb3rs import validate
def test_lenth():
    assert validate("1.1.1") == False
    assert validate("1.1") == False
    assert validate("1") == False
    assert validate("1.10.1.1") == True

def test_range():
    assert validate("275.2.3.10") == False
    assert validate("1.10000.3.30") == False
    assert validate("10000.36.36.36") == False
    assert validate("1.10.1.1") == True

def test_decimal():

    assert validate("1.10.1.1") == True
