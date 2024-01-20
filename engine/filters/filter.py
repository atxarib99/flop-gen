from abc import ABC, abstractmethod
class Filter(ABC):

    def __init__(self, filter_val):
        self.filter_val = filter_val

    @abstractmethod
    def check():
        pass

