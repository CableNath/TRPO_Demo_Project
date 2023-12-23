# Функция: calculate_average(numbers)
def calculate_average(numbers):
    if len(numbers) == 0:
        print()
        return None
    return sum(numbers) / len(numbers)

