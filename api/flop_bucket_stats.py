from Deck import Deck
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
generate = 1000000

monotone_filter = [Texture('m')]
paired_filter = [Pairing('unpaired').invert()]
connected_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('connected')]
high_gutshot_possible_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('semi_connected_high'), HighestCardAtLeast(11)]
low_not_connected_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('connected').invert(), HighestCard(10)]
high_no_gutshot_possible_filter = [Texture('m').invert(), Pairing('unpaired'), Connectivity('semi_connected_high').invert(), Connectivity('connected').invert(), HighestCardAtLeast(11)]

all_buckets = [monotone_filter, paired_filter, connected_filter, high_gutshot_possible_filter, low_not_connected_filter, high_no_gutshot_possible_filter]
counts = [0] * len(all_buckets)

fits_none_count = 0
fits_multiple_count = 0

while generate > 0:
    deck = Deck(numdecks=1)
    board = (deck.nextCard(), deck.nextCard(), deck.nextCard())

    fits_count = 0
    for i, bucket in enumerate(all_buckets):
        if all([filter.validate(board) for filter in bucket]):
            counts[i] += 1
            fits_count += 1
    if fits_count == 0:
        fits_none_count += 1
    elif fits_count > 1:
        fits_multiple_count += 1

    #always decrement
    generate-=1

counts = [x/sum(counts) for x in counts]

print(counts)
print(fits_none_count, fits_multiple_count)