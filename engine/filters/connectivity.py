
from Card import Card
from filters.filter import Filter
class Connectivity(Filter):

    def __init__(self, connectivity: str):
        self.valid_input(connectivity)
        self.connectivity = connectivity
        
        Filter.__init__(self, filter_val=connectivity)


    def check(self, board):
        if self.connectivity == 'unconnected':
            #each card must be at least 5 apart
            return self.distance(board, 5)
        if self.connectivity == 'semi':
            #each card must be at least 4 apart
            return self.distance(board, 4)
        if self.connectivity == 'full':
            #each card must be at least 3 apart
            return self.distance(board, 3)

    def distance(self, board, distance):
        if abs(board[0].evaluate() - board[1].evaluate()) > distance:
            return False
        if abs(board[1].evaluate() - board[2].evaluate()) > distance:
            return False
        if abs(board[0].evaluate() - board[2].evaluate()) > distance:
            return False

        return True

    def valid_input(self, connectivity):
        assert connectivity == 'unconnected' or connectivity == 'semi' or connectivity == 'full', "Texture must be one of the following: (unconnected, semi, full)"

