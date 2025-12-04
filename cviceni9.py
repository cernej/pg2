def nejvetsi(seznam_cisel):
    return 0


def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([100, 50, 30, 10]) == 100
    assert nejvetsi() == None