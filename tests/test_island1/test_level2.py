
from poetry_tutorial.island1.level2 import first_word

def test_lvel2_1():
    assert first_word("Hello world") == "Hello"
    
def test_lvel2_2():
    assert first_word("a word") == "a"

def test_lvel2_3():
    assert first_word("greeting from CheckiO Planet") == "greeting"

def test_lvel2_4():
    assert first_word("hi") == "hi"

