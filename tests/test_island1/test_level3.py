
from poetry_tutorial.island1.level3 import is_acceptable_password

def test_level3_1():
    assert is_acceptable_password("short") == False

def test_level3_2():
    assert is_acceptable_password("muchlonger") == True

def test_level3_3():
    assert is_acceptable_password("ashort") == False

