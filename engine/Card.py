class Card:
    def __init__(self, suit, char):
        self.suit = suit
        self.char = char
    
    def evaluate(self):
        #todo Dynamic aces
        if self.char == 'A':
            return 14
        if self.char == 'K':
            return 13
        if self.char == 'Q':
            return 12
        if self.char == 'J':
            return 11
        if self.char == 'T':
            return 10
        else:
            return int(self.char)

    def __eq__(self, other):
        return (self.suit == other.suit and self.char == other.char)

    def __hash__(self):
        suit_val = ['Club', 'Spade', 'Heart', 'Diamond'].index(self.suit)
        return self.evaluate() << suit_val

    def __str__(self):
        return str(self.char) + ' of ' + self.suit

    def __repr__(self):
        return str(self)
