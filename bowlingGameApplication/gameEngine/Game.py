# Abstract class: Game
import abc


class Game(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def roll(self, pins):
        return

    @abc.abstractmethod
    def score(self):
        return
