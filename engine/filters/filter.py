from abc import ABC, abstractmethod
class Filter(ABC):

    def __init__(self, filter_val):
        self.filter_val = filter_val
        self.isInverted = False

    @abstractmethod
    def check(self, Board):
        pass

    def invert(self):
        self.isInverted = True

    def validate(self, Board):
        output = self.check(Board)
        return ((not output) if self.isInverted else output)


