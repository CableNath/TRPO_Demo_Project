
import pytest
from services.factorial import *
from services.palindrome import *
from services.priority import *
from services.reverse import *

# Тесты для функции factorial(n)
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

# Тесты для функции is_prime(n)
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(15) == False


# Тесты для функции reverse_string(s)
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""

# Тесты для функции is_palindrome(s)
def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True
