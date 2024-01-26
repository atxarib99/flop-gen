from filters.filter import Filter
class HighestCardAtLeast(Filter):

    def __init__(self, highest_card_at_least):
        
        Filter.__init__(self, filter_val=highest_card_at_least)


    def check(self, board):
        for card in board:
            if card.evaluate() >= self.filter_val:
                return True
        return False
