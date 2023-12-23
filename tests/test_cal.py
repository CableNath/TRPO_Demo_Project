from services.calculate import *

# Тесты для функции calculate_average(numbers)
def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) != 3.0
    assert calculate_average([10, 20, 30, 40, 50]) != 30.0
    assert calculate_average([]) == None