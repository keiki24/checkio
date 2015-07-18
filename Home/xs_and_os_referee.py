def checkio(game_result):
    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    zipped = list(zip(game_result[0], game_result[1], game_result[2]))
    for col in zipped:
        if col[0] == col[1] == col[2] and col[0] != '.':
            return col[0]
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != '.':
        return game_result[0][2]
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
