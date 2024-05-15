from filters.filter import Filter
class HighestCardAtLeast(Filter):

    options = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, highest_card_at_least):
        self.valid_input(highest_card_at_least)
        
        Filter.__init__(self, filter_val=highest_card_at_least)


    def check(self, board):
        for card in board:
            if card.evaluate() >= self.filter_val:
                return True
        return False
