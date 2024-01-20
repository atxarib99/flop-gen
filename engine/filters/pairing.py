
from filters.filter import Filter
from Card import Card
class Pairing(Filter):

    def __init__(self, pairing: str):
        self.valid_input(pairing)
        
        Filter.__init__(filter_val=pairing)


    def check(self, board):
        if self.pairing == 'unpaired':
            return len(set([card.evaluate() for card in board])) == 3
        if self.pairing == 'paired':
            return len(set([card.evaluate() for card in board])) == 2
        if self.pairing == 'tripled':
            return len(set([card.evaluate() for card in board])) == 1

    def valid_input(self, pairing):
        assert pairing == 'unpaired' or pairing == 'paired' or pairing == 'tripled', "Texture must be one of the following: (unpaired, paired, tripled)"

