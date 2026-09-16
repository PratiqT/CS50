from LECTURE_TEST06.test_plates.plates import is_valid
def test_charecters():
    assert is_valid("CS501234") == False
    assert is_valid("CS5012") == True
    assert is_valid("c") == False

def test_start_with_letters():
    assert is_valid("12345") == False
    assert is_valid("CS5012") == True

def test_puntuations():
    assert is_valid("CS50 1") == False
    assert is_valid("CS50!1") == False
    assert is_valid("CS5012") == True

def test_startswith0():
    assert is_valid("CS05") == False
    assert is_valid("CS5012") == True
def test_no_LETTER_after_NUMBER():
    assert is_valid("CS50CS50") ==  False
    assert is_valid("AA2BB") ==  False
    assert is_valid("CS50CS") ==  False
    assert is_valid("CS5012") == True


