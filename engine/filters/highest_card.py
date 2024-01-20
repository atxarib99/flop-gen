
from filters.filter import Filter
from Card import Card
class HighestCard(Filter):

    def __init__(self, highest_card: Card):
        
        Filter.__init__(self, filter_val=highest_card)


    def check(self, board):
        for card in board:
            if card.evaluate() > self.filter_val:
                return False
        return True
        


