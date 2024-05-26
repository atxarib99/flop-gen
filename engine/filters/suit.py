
from .filter import Filter
class Suit(Filter):

    options = ["Club", "Spade", "Heart", "Diamond"]

    def __init__(self, suit: str):
        self.valid_input(suit)
        Filter.__init__(self, filter_val=suit)

    def check(self, board):
        for card in board:
            if card.suit != self.filter_val:
                return False
        return True

