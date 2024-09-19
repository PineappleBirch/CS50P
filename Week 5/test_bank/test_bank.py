import bank

def test_bank():

    assert bank.value('  hello ') == 0
    assert bank.value('hello') == 0
    assert bank.value('HeLlO') == 0
    assert bank.value('  HeLlO ') == 0
    assert bank.value('Hiya') == 20
    assert bank.value(' Hi') == 20
    assert bank.value('Honolulu') == 20
    assert bank.value('Whats up') == 100
    assert bank.value(' sup') == 100
