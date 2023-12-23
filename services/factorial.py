
# Функция: factorial(n)
def factorial(n):
    if n == 0:
        print()
        return 1
    else:
        return n * factorial(n - 1)
