
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

# empty_location checks if there are empty cells in the board; if not empty it returns the empty location
def empty_location(board, loc):
    for i in range(9):
        for j in range(9):
            if str(board[i][j]) == str(0):
                loc[0] = i
                loc[1] = j
                return True
    return False

def can_place_row(a, r, n):
    for i in range(9):
        if str(a[r][i]) == str(n):
            return False
    return True

def can_place_col(a, c, n):
    for i in range(9):
        if str(a[i][c]) == str(n):
            return False
    return True

def can_place_box(a, r, c, n):
    for i in range(3):
        for j in range(3):
            if str(a[i+r][j+c]) == str(n):
                return False
    return True

# is_valid checks if num can be placed in the row, col position
def is_safe_location(board, row, col, num):
    return (can_place_row(board, row, num) and
            can_place_col(board, col, num) and
            can_place_box(board, row-row%3, col-col%3, num))

def solve(board):
    loc = [0, 0]
    if not empty_location(board, loc):
        return True
    empty_row = loc[0]
    empty_col = loc[1]
    for i in range(1, 10):
        if is_safe_location(board, empty_row, empty_col, i):
            board[empty_row][empty_col] = i
            if solve(board):
                return True
            board[empty_row][empty_col] = 0
    return False

if __name__ == "__main__":
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    if solve(board):
        print_board(board)
    else:
        print("cannot solve input board")