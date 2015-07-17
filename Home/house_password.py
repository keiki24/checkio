def checkio(data):
    isuuper = False
    islower = False
    isdigit = False

    # パスワードが10文字以上か
    if len(data) < 10:
        return False
    # 大文字が1文字でも含まれているか
    for i in data:
        if i.isupper():
            isuuper = True
    for i in data:
        if i.islower():
            islower = True
    # 数字が1文字でも含まれているか
    for n in data:
        if n.isdigit():
            isdigit = True
    if isuuper and islower and isdigit:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
