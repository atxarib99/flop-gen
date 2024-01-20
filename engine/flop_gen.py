from Deck import Deck
from filters.highest_card import HighestCard
from filters.suit import Suit
from filters.texture import Texture

deck = Deck(numdecks=1)

my_filters = []
board = ()
boards = []

#A,K,....,10,9
highest_card = None

#r,tt,m
texture = None

#suit
suit = None

#unpaired, paired, tripled
pairing = None

#unconnected, semi, full
connectivity = None

#provide weights
weights = False

#how many to generate
generate = 5

my_filters.append(HighestCard(8))
my_filters.append(Texture('m'))
my_filters.append(Suit('Heart'))

if weights:
    while generate > 0:
        deck = Deck(numdecks=1)
        board = (deck.nextCard(), deck.nextCard(), deck.nextCard())
        #check if any filters are invalidated
        if False in [True if filter.check(board) else False for filter in my_filters]:
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
        if False in [True if filter.check(board) else False for filter in my_filters]:
            continue
        #otherwise check if board already in previous
        exists = False
        for gen_board in boards:
            if gen_board == board:
                exists = True
                break

        #only decrement if board is unique
        if not exists:
            boards.append(set(board))
            generate-=1


#psudo: add cards 1 at a time, after each deck.remove(card) if not filter.check(board+card) for filter in filters


print(boards)
