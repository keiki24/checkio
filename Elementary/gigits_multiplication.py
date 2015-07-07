def checkio(number):
    x = 1
    for i in str(number):
        i = int(i)
        if i:
            x *= i
    return x

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
