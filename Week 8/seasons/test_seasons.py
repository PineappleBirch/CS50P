from seasons import verbalize

def test_verbalize():
    assert verbalize(3) == 'three'
    assert verbalize(42) == 'forty-two'
    assert verbalize(511) == 'five hundred eleven'
