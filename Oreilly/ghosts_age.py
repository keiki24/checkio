def checkio(opacity):
    mxv = 10000
    rv = 0
    if opacity == mxv:
        rv = 0
    fibonacci = get_fibonacci()
    for i in range(1, mxv):
        if i in fibonacci:
            mxv = mxv - i
        else:
            mxv += 1
        if opacity == mxv:
            rv = i

    return rv

def get_fibonacci():
    fibo_list = []
    bnum = 1
    bbnum = 1
    fibo_list.append(bnum)
    fibo_list.append(bbnum)

    for i in range(2, 10000):
        if i == (bnum + bbnum):
            fibo_list.append(i)
            bbnum = bnum
            bnum = i
    return fibo_list

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
