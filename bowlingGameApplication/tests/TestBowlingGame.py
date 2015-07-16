import unittest
from bowlingGameApplication.gameEngine.BowlingGame import BowlingGame


class TestBowlingGame(unittest.TestCase):
    """ UnitTests case for Bowling Game
    """

    def setUp(self):
        self.game = BowlingGame()

    def _rollMany(self, number_of_games, pins):
        for i in xrange(number_of_games):
            self.game.roll(pins)

    def _rollSpare(self):
        self.game.roll(6)
        self.game.roll(4)

    def _rollStrike(self):
        self.game.roll(10)

    def testGutterGame(self):
        print("Test Gutter Game")
        self._rollMany(20, 0)
        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        print("Test when pins hit across all games is 1")
        self._rollMany(20, 1)
        self.assertEqual(20, self.game.score())

    def testOneSpare(self):
        print("Test when one spare is hit")
        self._rollSpare()
        self.game.roll(4)
        self._rollMany(17, 0)
        self.assertEqual(18, self.game.score())

    def testOneStrike(self):
        print("Test when one strike is hit")
        self._rollStrike()
        self.game.roll(5)
        self.game.roll(3)
        self._rollMany(16, 0)
        self.assertEqual(26, self.game.score())

    def testPerfectGame(self):
        print("Test perfect gameEngine when all is strike")
        self._rollMany(12, 10)
        self.assertEqual(300, self.game.score())

    def testArbitraryValue(self):
        print("Test with arbitrary values")
        self.game.roll(5)
        self._rollSpare()
        self._rollStrike()
        self._rollMany(17, 3)
        self.assertEqual(73, self.game.score())

    def testRolledMoreThanPermitted(self):
        print("Test Exception Case")
        self._rollMany(22, 0)
        self.assertRaises(IndexError, self.game.score)
