
from filters.filter import Filter
from Card import Card
class Suit(Filter):

    def __init__(self, suit: str):
        
        Filter.__init__(self, filter_val=suit)

    def check(self, board):
        for card in board:
            if card.suit != self.filter_val:
                return False
        return True
        


