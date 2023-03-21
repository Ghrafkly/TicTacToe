def start():
    board = gen_board()
    turn = 0
    won = False
    used = []

    while not won:
        display_board(board, turn)
        board = take_turn(board, turn, used)
        won = win(board, turn)
        turn += 1

    if won:
        if turn % 2 == 0:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")


def take_turn(board, turn, used):
    row = input("Row (1-3): ")
    col = input("Col (1-3): ")

    while not row.isdigit() \
            or not col.isdigit() \
            or int(row) not in range(1, 4) \
            or int(col) not in range(1, 4) \
            or (row, col) in used:
        print("Invalid input")
        row = input("Row (1-3): ")
        col = input("Col (1-3): ")

    used.append((row, col))

    row = int(row)
    col = int(col)

    if turn % 2 == 0:
        board[row - 1][col - 1] = "x"
    else:
        board[row - 1][col - 1] = "o"
    return board


def win(board, turn):
    x, o = [], []

    for row_id, row in enumerate(board):
        for col_id, col in enumerate(row):
            if col == "x":
                x.append(row_id * 10 + col_id)
            elif col == "o":
                o.append(row_id * 10 + col_id)

    if turn % 2 == 0:
        return checks(x)
    else:
        return checks(o)


def checks(player):
    h = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    v = [[0, 10, 20], [1, 11, 21], [2, 12, 22]]
    d = [[0, 11, 22], [2, 11, 20]]

    c = [h, v, d]

    for item in c:
        for i in item:
            if all(x in player for x in i):
                return True
    return False


def display_board(board, turn):
    print(f"Turn: {turn}")
    for row in board:
        print(row)


def gen_board():
    return [["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]


if __name__ == "__main__":
    start()
