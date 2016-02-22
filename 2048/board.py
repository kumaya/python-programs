import random


class Board(object):
    """ Returns a new partially-empty board for 2048.
     Contains number 2 generated at random place in the board
    """
    __row = 4
    __column = 4

    def __init__(self):
        self.__board = None

    def get_new_board(self):
        self.__board = [[0 for _ in range(Board.__column)] for _ in range(Board.__row)]
        random_row = random.randint(0, Board.__row-1)
        random_column = random.randint(0, Board.__column-1)
        self.__board[random_row][random_column] = 2
        return self.__board

    def draw(self):
        print "Board: "
        for i in range(Board.__row):
            for j in range(Board.__column):
                print self.__board[i][j],
            print


if __name__ == "__main__":
    board = Board()
    board.get_new_board()
    board.draw()
