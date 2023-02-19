import numpy as np

board = [
    [8, 4, 9, 0, 0, 3, 5, 7, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 9, 0, 0, 8, 3],
    [0, 0, 0, 9, 4, 6, 7, 0, 0],
    [0, 8, 0, 0, 5, 0, 0, 4, 0],
    [0, 0, 6, 8, 7, 2, 0, 0, 0],
    [5, 7, 0, 0, 1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 2, 1, 7, 0, 0, 8, 6, 5]
]

def possible(row, col, n):
    for c in range(9):
        if board[row][c] == n:
            return False
    for r in range(9):
        if board[r][col] == n:
            return False
    box_row = (row//3)*3
    box_col = (col//3)*3
    for r in range(3):
        for c in range(3):
            if board[box_row+r][box_col+c] == n:
                return False
    return True

def solve(row=0, col=0):

    if (row == 8 and col == 9):
        return True

    if col == 9:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solve(row, col + 1)

    for n in range(1, 10):
        if possible(row, col, n):
            board[row][col] = n
            if solve(row, col + 1):
                return True
        board[row][col] = 0

    return False

solve()
print(np.matrix(board))
