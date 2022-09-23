
from poetry_tutorial.island1.level1 import mult_two

def test_level1_1():
    assert mult_two(3, 2) == 6
    
def test_level1_2():
    assert mult_two(0, 1) == 0
