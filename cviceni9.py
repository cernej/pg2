def nejvetsi(seznam_cisel):
    if not seznam_cisel:
        return None
    return max(seznam_cisel)


def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([100, 50, 30, 10]) == 100
    assert nejvetsi([]) == None