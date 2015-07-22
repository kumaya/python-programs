# Class to run the bowling application
from bowlingGameApplication.gameEngine.BowlingGameFactory import GameFactory
from bowlingGameApplication.userEngine.UserFactory import UserFactory
import random


class PlayGame(object):
    def __init__(self, players):
        self.players = players

    def invoke_game(self):
        users = UserFactory().get_players(self.players)
        games = GameFactory().get_games(len(users))
        users = self.run(games, users)
        max_score = 0
        user = 0
        for i in range(len(users)):
            if users[i].get_score() > max_score:
                max_score = users[i].get_score()
                user = i
        print("Winner is User %d with score of %d" % (user, max_score))

    def run(self, games, users):
        for i in range(len(users)):
            j = 1
            while j <= 21:
                val = random.randint(1, 10)
                if val == 10:
                    j += 1
                if j%2 != 0 and val != 10:
                    val = 10 - val
                print ("User %d scored %d %d" % (i, val, j))
                games[i].roll(val)
                j += 1
        for i in range(len(users)):
            users[i].set_score(games[i].score())
        return users


if __name__ == "__main__":
    num_of_players = input("Enter the number of players: ")
    game = PlayGame(num_of_players)
    game.invoke_game()