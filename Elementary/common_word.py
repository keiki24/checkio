def checkio(first, second):
    words = []
    rv = ","
    words_second = [t.lower() for t in second.split(",")]
    for word_first in first.split(","):
        if word_first.lower() in words_second:
            words.append(word_first)
    return rv.join(sorted(words))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
