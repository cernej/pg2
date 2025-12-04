import pytest

def operace(typ, a, b):
    if typ == '+':
        return a + b
    elif typ == '-':
        return a - b
    elif typ == '*':
        return a * b
    elif typ == '/':
        if b == 0:
            raise ZeroDivisionError('Nelze delit nulou')
        return a / b
    

def test_operace():
    assert operace('+', 1, 1) == 2
    assert operace('-', 5, 3) == 2
    assert operace('*', 2, 2) == 4
    assert operace('/', 6, 2) == 3
    with pytest.raises(ZeroDivisionError) as e:
        operace('/', 1, 0)
    assert 'Nelze delit nulou' in str(e.value)


if __name__ == "__main__":
    test_operace()