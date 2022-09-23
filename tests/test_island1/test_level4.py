
from poetry_tutorial.island1.level4 import number_length

def test_level4_1():
    assert number_length(10) == 2

def test_level4_2():
    assert number_length(0) == 1

def test_level4_3():
    assert number_length(4) == 1

def test_level4_4():
    assert number_length(44) == 2


