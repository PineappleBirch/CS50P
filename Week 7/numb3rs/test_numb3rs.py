from numb3rs import validate

def test_validate_true():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True


def test_validate_false():
    assert validate('1.2.3.1000') == False
    assert validate('34.678.325.672') == False
    assert validate('cat') == False
