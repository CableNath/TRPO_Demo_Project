
# Функция: factorial(n)
def factorial(n):
    if n == 0:
        print()
        return 1
    else:
        return n * factorial(n - 1)


# Функция: is_prime(n)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Функция: reverse_string(s)
def reverse_string(s):
    return s[::-1]

# Функция: is_palindrome(s)
def is_palindrome(s):
    return s == s[::-1]



# Функция: calculate_average(numbers)
def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
