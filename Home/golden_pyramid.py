def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    pyramid = [list(t) for t in pyramid]
    for i in range(1, len(pyramid)):
        for j in range(len(pyramid[i])):
            up_right = 0 if j >= len(pyramid[i-1]) else pyramid[i-1][j]
            up_left = 0 if j == 0 else pyramid[i-1][j-1]
            pyramid[i][j] += max(up_right, up_left)

    return max(pyramid[-1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
