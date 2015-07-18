def checkio(text):
    max_num = 0
    a = ""
    text = text.lower()
    for i in text:
        if i.isalpha():
            if text.count(i) > max_num:
                max_num = text.count(i)
                a = i
            if text.count(i) == max_num:
                a = min(a, i)
    return a

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
