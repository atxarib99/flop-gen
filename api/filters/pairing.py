
from filters.filter import Filter
from Card import Card
class Pairing(Filter):

    options = ["unpaired", "paired", "tripled"]

    def __init__(self, pairing: str):
        self.valid_input(pairing)
        self.pairing = pairing
        Filter.__init__(self, filter_val=pairing)


    def check(self, board):
        if self.pairing == 'unpaired':
            return len(set([card.evaluate() for card in board])) == 3
        if self.pairing == 'paired':
            return len(set([card.evaluate() for card in board])) == 2
        if self.pairing == 'tripled':
            return len(set([card.evaluate() for card in board])) == 1

