from bowlingGameApplication.gameEngine.BowlingGame import BowlingGame


class GameFactory(object):
    @staticmethod
    def get_bowling_game():
        return BowlingGame()

    def get_games(self, num_of_games):
        bowling_games = []
        for i in range(num_of_games):
            bowling_games.append(self.get_bowling_game())
        return bowling_games
