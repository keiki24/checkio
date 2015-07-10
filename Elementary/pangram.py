def check_pangram(text):
    atoz = [chr(i) for i in range(ord('a'), ord('z')+1)]
    for s in text:
        if s.lower() in atoz:
            atoz.remove(s.lower())
        if len(atoz) == 0:
            return True
    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
