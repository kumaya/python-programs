from bowlingGameApplication.userEngine.user import User


class UserFactory(object):
    """ Factory class to generate and return total
     players for the game
    """

    @staticmethod
    def get_user():
        return User()

    def get_players(self, num_of_players):
        all_players = []
        for player in range(num_of_players):
            all_players.append(self.get_user())
        return all_players
