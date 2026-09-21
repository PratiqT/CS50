from um import count


def test_single_um():
    assert count("um") == 1


def test_multiple_um():
    assert count("um um") == 2


def test_case_insensitive():
    assert count("Um uM UM um") == 4


def test_with_punctuation():
    assert count("Hello, um, world!") == 1


def test_at_beginning():
    assert count("um hello") == 1


def test_at_end():
    assert count("hello um") == 1


def test_no_um():
    assert count("hello world") == 0


def test_inside_word():
    assert count("yummy album umbrella") == 0


def test_mixed():
    assert count("Um, thanks. um? UM!") == 3


def test_empty_string():
    assert count("") == 0