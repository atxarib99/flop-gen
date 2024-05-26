from .Deck import Deck
from .Card import Card
from .filters.highest_card import HighestCard
from .filters.suit import Suit
from .filters.pairing import Pairing
from .filters.texture import Texture
from .filters.connectivity import Connectivity
from .filters.highest_card_at_least import HighestCardAtLeast

def generate(filters: list, engine_parms: dict):
    deck = Deck(numdecks=1)

    my_filters = []
    board = ()
    boards = []

    def board_compare(board, other):
        #check if they are the same cards and same tone
        def get_tone(board):
            suits = (board[1],board[3],board[5])
            if len(set(suits)) == 2:
                return 'tt'
            elif len(set(suits)) == 3:
                return 'r'
            elif len(set(suits)) == 1:
                return 'm'
            print('youre an absolute dumbass somehow')
            print(board)

        board_str = ''.join([str(card) for card in reversed(sorted(list(board), key=(lambda card: card.evaluate())))])
        other_str = ''.join([str(card) for card in reversed(sorted(list(other), key=(lambda card: card.evaluate())))])

        board_f = board_str[0] + board_str[2] + board_str[4] + get_tone(board_str)
        other_f = other_str[0] + other_str[2] + other_str[4] + get_tone(other_str)
        if board_f == other_f:
            return True
        return False

    #provide weights
    weights = bool(engine_parms['weights'])

    #how many to generate
    generate = int(engine_parms['flops'])

    #set filters
    my_filters = filters

    if weights:
        # Generate 1m flops
        while generate > 0:
            deck = Deck(numdecks=1)
            board = (deck.nextCard(), deck.nextCard(), deck.nextCard())
            #check if any filters are invalidated
            if False in [True if filter.validate(board) else False for filter in my_filters]:
                continue
            #otherwise check if board already in previous
            exists = False
            for gen_board in boards:
                if gen_board[0] == board:
                    gen_board[1]+=1
                    exists = True
                    break

            if not exists:
                boards.append((set(board), 1))

            #always decrement
            generate-=1
    else:
        while generate > 0:
            deck = Deck(numdecks=1)
            board = (deck.nextCard(), deck.nextCard(), deck.nextCard())
            #check if any filters are invalidated
            if False in [True if filter.validate(board) else False for filter in my_filters]:
                continue
            #otherwise check if board already in previous
            exists = False
            for gen_board in boards:
                #if gen_board == board:
                if board_compare(gen_board, board):
                    exists = True
                    break

            #only decrement if board is unique
            if not exists:
                boards.append(set(board))
                generate-=1
            
    sorted_boards = []
    for board in boards:
        sorted_board = ""
        for card in reversed(sorted(list(board), key=(lambda card: card.evaluate()))):
            sorted_board += str(card)
        sorted_boards.append(sorted_board)

    return sorted_boards


