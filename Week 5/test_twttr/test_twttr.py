import twttr

def test_twttr():

    assert twttr.shorten('Hello, World!') == 'Hll, Wrld!'
    assert twttr.shorten('CS50') == 'CS50'
    assert twttr.shorten('AEIOU') == ''
