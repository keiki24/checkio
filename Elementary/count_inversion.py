def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for i, n in enumerate(sequence):
        if i or i < len(sequence):
            for x in range(1, i+1):
                if sequence[i-x] > sequence[i]:
                    count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
