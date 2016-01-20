from MineSweeperGame.board import Board


class TextBoard(Board):
    def __init__(self, width, height, numMines):
        self.width = width
        self.height = height
        self.numMines = numMines
        super(TextBoard, self).__init__(width, height, numMines)

    def new_text_board(self):
        try:
            self.numOfCellsUnknown = self.width * self.height
            if self.numOfCellsUnknown < self.numMines:
                raise ValueError("numMines cannot be greater then number of Unknown cells")
            else:
                self.new_board()
        except ValueError:
            raise


    def draw(self):
        print ""
        print "  ",
        for i in xrange(self.width):
            print("%d" %i),
        print("\n")
        for i in xrange(self.width):
            print("%d " %i),
            for j in xrange(self.height):
                if self.board[i][j] == self.UNKNOWN:
                    print "#",
                elif self.board[i][j] == self.MARKED:
                    print "X",
                elif self.board[i][j] == self.MINE:
                    print "*",
                elif self.board[i][j] == 0:
                    print ".",
                else:
                    print self.board[i][j],
            print ""
        print("Mines remaining: %d" %(self.get_mines()- self.get_marked()))
        print("Unknown cells remaining: %d" % self.get_unknown())
        print ""