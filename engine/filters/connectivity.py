
from Card import Card
from filters.filter import Filter
class Connectivity(Filter):

    def __init__(self, connectivity: str):
        self.valid_input(connectivity)
        self.connectivity = connectivity
        Filter.__init__(self, filter_val=connectivity)


    def check(self, board):
        # board sorted low to high
        sorted_board = sorted(list(board), key=(lambda card: card.evaluate()))

        if self.connectivity == 'disconnected':
            return self.distance(board, 5)
        if self.connectivity == 'semi_connected_low':
            return sorted_board[1].evaluate() - sorted_board[0].evaluate() <= 4 and not(sorted_board[2].evaluate() - sorted_board[0].evaluate() <= 4)
        if self.connectivity == 'semi_connected_high':
            return (sorted_board[2].evaluate() - sorted_board[1].evaluate() <= 4) and not(sorted_board[2].evaluate() - sorted_board[0].evaluate() <= 4)
        if self.connectivity == 'connected':
            return sorted_board[2].evaluate() - sorted_board[0].evaluate() <= 4
        
    def distance(self, board, distance):
        if abs(board[0].evaluate() - board[1].evaluate()) < distance:
            return False
        if abs(board[1].evaluate() - board[2].evaluate()) < distance:
            return False
        if abs(board[0].evaluate() - board[2].evaluate()) < distance:
            return False

        return True

    def valid_input(self, connectivity):
        assert connectivity in ['disconnected', 'semi_connected_low', 'semi_connected_high', 'connected'], "Texture must be one of the following: ('disconnected', 'semi_connected_low', 'semi_connected_high', 'connected')"

