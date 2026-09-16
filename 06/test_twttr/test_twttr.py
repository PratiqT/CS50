from LECTURE_TEST06.test_twttr.twttr import shorten

def test_uppercase_vovels():
    assert shorten("AEIOU") == ''

def test_lowercase_vovels():
    assert shorten("aeiou") == ''

def test_twiter():
    assert shorten("twitter") == "twttr"

def test_numbers():
    assert shorten("1") == "1"

def test_punctuation():
    assert shorten("hello!") == "hll!"