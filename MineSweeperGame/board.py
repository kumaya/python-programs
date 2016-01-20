import abc
import random


class Board(object):
    """ This class implements the basic behaviour of the MineSweeper game; grid
    of cells which may contain a mine, intially covered and phase by phase
    revealed. Revealed cells contain a mine or number representing number of
    mines in upto eight adjacent cells. The cells can also be marked, to
    indicate cells that might contain a mine.

    :param height = Height of the board
    :param width = Width of the board
    :param numMines = Number of mines in the board; randomly distributed
    """
    __metaclass__ = abc.ABCMeta

    # Constants for cell contents
    UNKNOWN = -1
    MARKED = -2
    MINE = -3

    def __init__(self, width=0, height=0, num_mines=0):
        # Board size
        self.width = width
        self.height = height

        # Number of mines in the board
        self.numMines = num_mines

        # Number of cells currently marked
        self.numOfCellsMarked = 0

        # Number of cells yet to be revealed
        self.numOfCellsUnknown = 0

        # cells containing information about mines
        self.__mines = []

        # current state of the board
        self.board = []

    def new_board(self):
        """ Returns a new board with given size and number of mines.
        :return: A new board containing randomly distributed mines
        """
        self.numOfCellsUnknown = self.width * self.height

        self.__mines = [[0] * self.height for i in xrange(self.width)]
        self.board = [[0] * self.height for i in xrange(self.width)]

        # clean the board
        for i in xrange(self.width):
            for j in xrange(self.height):
                self.__mines[i][j] = False
                self.board[i][j] = self.UNKNOWN

        # Randomly allocate mines in the cells
        temp = 0

        while temp < self.numMines:
            cellw = random.randint(0, self.width-1)
            cellh = random.randint(0, self.height-1)
            if not self.__mines[cellw][cellh]:
                self.__mines[cellw][cellh] = True
                temp += 1

    @abc.abstractmethod
    def draw(self):
        """ Representation of the board. Can be UI/human understable format.
        Need to be implemented by subclass
        """
        pass

    def nearby_mines(self, x, y):
        """ find number of mines in the neighbourhood of x and y
        """
        result = 0
        maxx, maxy, minx, miny = self.boundary(x, y)
        for i in xrange(minx, maxx):
            for j in xrange(miny, maxy):
                if self.__mines[i][j]:
                    result += 1
        return result

    def boundary(self, x, y):
        minx = 0 if x <= 0 else x - 1
        maxx = x if x >= (self.width - 1) else x + 2
        miny = 0 if y <= 0 else y - 1
        maxy = y if y >= (self.height - 1) else y + 2
        return maxx, maxy, minx, miny

    def reveal(self, x, y):
        """ reveal the contents of a cell.
        :return: number from 0..8 or special cell marked MINE
        """
        if self.board[x][y] == self.MARKED:
            self.numOfCellsMarked -= 1
        elif self.board[x][y] == self.UNKNOWN:
            self.numOfCellsUnknown -= 1
            if self.__mines[x][y]:
                self.board[x][y] = self.MINE
            else:
                self.board[x][y] = self.nearby_mines(x, y)
        return self.board[x][y]

    def reveal_more(self, x, y):
        """reveal the contents of more cell around a given cell.
        If the cell contents are currently unknown and cell does not contain a mine, the
        contents of cell are revealed.
        if revealed cell is empty and has no neighbouring mines, reveal_more is called
        recursively.
        """
        maxx, maxy, minx, miny = self.boundary(x, y)
        for i in xrange(minx, maxx):
            for j in xrange(miny, maxy):
                if (not self.__mines[i][j]) and self.board[i][j] == self.UNKNOWN:
                    self.reveal(i, j)
                    if self.board[i][j] == 0:
                        self.reveal_more(i, j)

    def marked(self, x, y):
        """ Mark the cell to indicate potentially indicate mine
        """
        if ((self.numMines - self.numOfCellsMarked) > 0) and self.board[x][y] == self.UNKNOWN:
            self.board[x][y] = self.MARKED
            self.numOfCellsMarked += 1
            return True
        else:
            return False

    def unmark(self, x, y):
        """ Unmark the marked cell
        """
        if self.board[x][y] == self.MARKED:
            self.board[x][y] = self.UNKNOWN
            self.numOfCellsMarked -= 1
            return True
        else:
            return False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_mines(self):
        return self.numMines

    def get_marked(self):
        return self.numOfCellsMarked

    def get_unknown(self):
        return self.numOfCellsUnknown