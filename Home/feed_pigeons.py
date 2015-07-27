def checkio(number):
    rv = 0
    for i in range(1, 100):
        pegions = int(i*(i+1)/2)
        for p in range(1, pegions+1):
            number = number - 1
            if p > rv:
                rv = p
            if number <= 0:
                return rv

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
