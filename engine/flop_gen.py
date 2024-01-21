from Deck import Deck
from Card import Card
from filters.highest_card import HighestCard
from filters.suit import Suit
from filters.pairing import Pairing
from filters.texture import Texture
from filters.connectivity import Connectivity
from filters.highest_card_at_least import HighestCardAtLeast

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
generate = 100

monotone_filter = [Texture('m')]
paired_filter = [Pairing('unpaired').invert()]
connected_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('connected')]
high_gutshot_possible_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('semi_connected_high'), HighestCardAtLeast(11)]
low_not_connected_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('connected').invert(), HighestCard(10)]
high_no_gutshot_possible_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('semi_connected_high').invert(), Connectivity('connected').invert(), HighestCardAtLeast(11)]

my_filters = high_gutshot_possible_filter

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
            if gen_board == board:
                exists = True
                break

        #only decrement if board is unique
        if not exists:
            boards.append(set(board))
            generate-=1


#psudo: add cards 1 at a time, after each deck.remove(card) if not filter.check(board+card) for filter in filters

for board in boards:
    sorted_board = reversed(sorted(list(board), key=(lambda card: card.evaluate())))
    for card in sorted_board:
        print(card, end="")
    print()

