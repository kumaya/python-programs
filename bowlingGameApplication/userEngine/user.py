
class User(object):
    """ Sets and returns the score of a user in a game
    """
    _score = 0

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score
