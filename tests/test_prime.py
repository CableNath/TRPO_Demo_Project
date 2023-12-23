from .services.priority import *

# Тесты для функции is_prime(n)
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(15) == False