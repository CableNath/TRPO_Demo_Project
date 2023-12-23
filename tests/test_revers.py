from .services.reverse import *

# Тесты для функции reverse_string(s)
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
