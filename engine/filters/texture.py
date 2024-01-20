
from filters.filter import Filter
from Card import Card
class Texture(Filter):

    def __init__(self, texture: str):
        self.valid_input(texture)
        
        Filter.__init__(self, filter_val=texture)


    def check(self, board):
        if self.filter_val == 'r':
            return len(set([card.suit for card in board])) == 3
        if self.filter_val == 'tt':
            return len(set([card.suit for card in board])) == 2
        if self.filter_val == 'm':
            return len(set([card.suit for card in board])) == 1

    def valid_input(self, texture):
        assert texture == 'r' or texture == 'tt' or texture == 'm', "Texture must be one of the following: (r, tt, m)"

