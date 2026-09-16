from LECTURE_TEST06.test_bank.bank import value
def test_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_h():
    assert value("hi") == 20
    assert value("How are you?") == 20

def test_other():
    assert value("What's up?") == 100
    assert value("good morning") == 100