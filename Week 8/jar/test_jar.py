from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar = Jar()
    assert jar.capacity == 12

    with pytest.raises(ValueError):
        jar = Jar(capacity = -1)

    with pytest.raises(ValueError):
        jar = Jar(capacity = 'cat')


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪🍪'


def test_deposit():
    jar = Jar(capacity = 8)
    jar.deposit(3)
    assert jar.size == 3

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

    jar = Jar(capacity = 8)
    with pytest.raises(ValueError):
        jar.deposit(9)


def test_withdraw():
    jar = Jar(capacity = 4)
    jar.deposit(3)
    assert jar.size == 3

    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)

    jar = Jar(capacity = 5)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)



