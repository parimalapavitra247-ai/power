from power import power

def test_power_1():
    assert power(2, 3) == 8

def test_power_2():
    assert power(4, 1) == 4

def test_power_3():
    assert power(5, 2) == 25
