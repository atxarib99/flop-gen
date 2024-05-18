from abc import ABC, abstractmethod
import itertools
class Filter(ABC):

    options = []

    def __init__(self, filter_val):
        self.filter_val = filter_val
        self.isInverted = False

    @abstractmethod
    def check(self, Board):
        pass

    def invert(self):
        self.isInverted = True
        return self

    def validate(self, Board):
        output = self.check(Board)
        return ((not output) if self.isInverted else output)

    def valid_input(self, inp):
        assert inp in self.options, (type(self).__name__ + " must be one of the following: " + str(self.options))


