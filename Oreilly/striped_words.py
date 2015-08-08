import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = filter(lambda w: len(w) > 0, re.split(r'\W+', text))
    num = 0
    for w in text:
        if is_striped(w):
            num += 1
    return num


def is_striped(word):
    if len(word) == 1:
        return False
    even = set(word[::2].upper())
    odd = set(word[1::2].upper())
    return (even.issubset(VOWELS) and odd.issubset(CONSONANTS)) or (odd.issubset(VOWELS) and even.issubset(CONSONANTS))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
