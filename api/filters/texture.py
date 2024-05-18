
from filters.filter import Filter
from Card import Card
class Texture(Filter):

    options = ["rainbow", "two-tone", "monotone"]

    def __init__(self, texture: str):
        self.valid_input(texture)
        
        Filter.__init__(self, filter_val=texture)


    def check(self, board):
        if self.filter_val == 'rainbow':
            return len(set([card.suit for card in board])) == 3
        if self.filter_val == 'two-tone':
            return len(set([card.suit for card in board])) == 2
        if self.filter_val == 'monotone':
            return len(set([card.suit for card in board])) == 1

