from .services.is_palindrome import *
# Тесты для функции is_palindrome(s)
def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True
