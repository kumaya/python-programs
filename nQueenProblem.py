# The N Queen is the problem of placing N chess queens on
# a NxN chessboard so that no two queens attack each other.
# Solution to the problem using Backtracking


def print_solution(board=[]):
    """ Function to print the solution
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            print "%s" % board[i][j],
        print ""


def is_safe(board=[], row=0, col=0):
    """ Function to check if queen can be placed in board[row][col].
    This function is called when 'col' queens are already placed in columns from 0 to -1.
    So we need to check only left side for attacking queen.
    """

    # Check the row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    return True


def solve_n_queen(board=[], col=0):
    """ Recursive function to solve n queen
    """

    # Base Case: When all queens are placed
    if col >= len(board):
        return True

    # Place queens in all rows of this col and check
    for i in range(len(board)):
        # Check if queen can be placed in ith row of col
        if is_safe(board, i, col):
            # If safe then place queen on board
            board[i][col] = 'X'

            # recur to place rest of queens
            if solve_n_queen(board, col+1) == True:
                return True
            board[i][col] = 0
    return False


if __name__ == "__main__":
    brd = [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
    if solve_n_queen(brd, 0) == False:
        print "Solution does not exist"
    else:
        print_solution(brd)
