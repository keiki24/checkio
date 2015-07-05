def checkio(words):
    words = words.split(" ")
    c = 0
    for i in words:
        if i.isalpha():
            c += 1
            if c >= 3:
                return True
        else:
            c = 0
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
