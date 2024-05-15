
from filters.filter import Filter
class HighestCard(Filter):

    options = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, highest_card):
        self.valid_input(highest_card)
        
        Filter.__init__(self, filter_val=highest_card)


    def check(self, board):
        for card in board:
            if card.evaluate() > self.filter_val:
                return False
        return True
        
