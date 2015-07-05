def count_words(text, words):
    c = 0
    for i in words:
        if i.lower() in text.lower():
            c += 1
    return c

assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
