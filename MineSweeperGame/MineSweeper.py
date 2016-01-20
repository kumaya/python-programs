from MineSweeperGame.TextBoard import TextBoard


class MineSweeper(object):
    DONE = False
    QUIT = False
    WON = False

    def __init__(self, width, height, numMines):
        self.width = width
        self.height = height
        self.numMines = numMines
        self.cur = 0

    def create_game(self):
        self.board = TextBoard(self.width, self.height, self.numMines)
        self.board.new_text_board()

    def play(self):
        while not self.DONE:
            self.board.draw()
            print "Command: ",
            command = raw_input("Enter REVEAL/MARK/UNMARK/QUIT: ")
            self.commands(command)

            if self.board.get_unknown() == self.board.get_mines():
                self.WON = True
                self.DONE = True
            elif self.cur == self.board.MINE:
                self.DONE = True

        if self.WON:
            print "May the force be with you"
        elif self.QUIT:
            print "You know nothing Jon Snow"
        else:
            print "FAILED"

        # Reveal everything at the end
        for i in xrange(self.width):
            for j in xrange(self.height):
                self.board.reveal(i, j)
        self.board.draw()

    def commands(self, command):
        cmd = str(command).lower()
        if cmd == "reveal":
            cellx, celly = map(int, raw_input("Enter cellx and celly: ").split())
            self.cur = self.board.reveal(cellx, celly)
            if self.cur == 0:
                self.board.reveal_more(cellx, celly)
        elif cmd == "mark":
            cellx, celly = map(int, raw_input("Enter cellx and celly: ").split())
            self.board.marked(cellx, celly)
        elif cmd == "unmark":
            cellx, celly = map(int, raw_input("Enter cellx and celly: ").split())
            self.board.unmark(cellx, celly)
        elif cmd == "help":
            print "*"*80
            print "Enter Reveal to reveal the contents of a cell"
            print "Enter Mark to mark any cell as possible mine"
            print "Enter Unmark to remove marked cell as possible mine"
            print "Enter quit to leave the show"
            print "*"*80
        elif cmd == "quit":
            self.QUIT = True
            self.DONE = True
        else:
            print "Unknown command, try 'help'"


if __name__ == "__main__":
    width, height, numMines = map(int, raw_input("Enter width, height and numberOfMines: ").split())
    game = MineSweeper(width, height, numMines)
    game.create_game()
    game.play()
