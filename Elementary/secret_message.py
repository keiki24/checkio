def find_message(text):
    strings = ""
    for i in text:
        if i.isupper():
            strings += i
    return strings


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary
    # for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
