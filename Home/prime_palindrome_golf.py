def golf(number):
    while True:
        number += 1
        if is_prime(number) and is_palindrome(number):
            return number
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def is_palindrome(number):
    number = str(number)
    n = len(number)
    for i in range(n//2):
        if not number[i] == number[-(i+1)]:
            return False
    return True
