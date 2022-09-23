
from poetry_tutorial.island1.level5 import most_frequent

def test_level5_1():
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

def test_level5_2():
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

