import plates

def test_plates1():
    assert plates.is_valid('CS50') == True

def test_plates2():
    assert plates.is_valid('CS05') == False
    assert plates.is_valid('CS50P') == False

def test_plates3():
    assert plates.is_valid('PI3.14') == False
    assert plates.is_valid('11') == False

def test_plates4():
    assert plates.is_valid('H') == False
    assert plates.is_valid('OUTATIME') == False

