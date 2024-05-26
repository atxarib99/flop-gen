
from .filter import Filter
class HighestCard(Filter):

    options = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, highest_card):
        self.valid_input(highest_card)
        
        Filter.__init__(self, filter_val=self.convert_to_int(highest_card))

    def convert_to_int(self, highest_card):
        if highest_card == 'T':
            return 10
        if highest_card == 'J':
            return 11
        if highest_card == 'Q':
            return 12
        if highest_card == 'K':
            return 13
        if highest_card == 'A':
            return 14

        return int(highest_card)


    def check(self, board):
        for card in board:
            if card.evaluate() > self.filter_val:
                return False
        return True
        
