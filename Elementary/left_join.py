def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    l = []
    for r in phrases:
        l.append(r.replace('right', 'left'))
    return ",".join(l)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
