FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number = str(number)
    length = len(number)
    rv = " "
    words = []
    if length == 1:
        words.append(FIRST_TEN[int(number[0])-1])
    if length == 2:
        if number[0] == '1':
            words.append(SECOND_TEN[int(number[1])])
        else:
            if number[1] == '0':
                words.append(OTHER_TENS[int(number[0])-2])
            else:
                words.append(OTHER_TENS[int(number[0])-2])
                words.append(FIRST_TEN[int(number[1])-1])
    if length == 3:
        words.append(FIRST_TEN[int(number[0])-1])
        words.append(HUNDRED)
        if number[1] == '0':
            if number[2] != '0':
                words.append(FIRST_TEN[int(number[2])-1])
        elif number[1] == '1':
            words.append(SECOND_TEN[int(number[2])])
        else:
            words.append(OTHER_TENS[int(number[1])-2])
            if number[2] != '0':
                words.append(FIRST_TEN[int(number[2])-1])
    rv = rv.join(words)
    return rv

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
