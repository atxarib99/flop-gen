from Card import Card
import random
import numpy as np

class Deck:
    def __init__(self, numdecks=6):
        self.numdecks = numdecks
        self.setupDeck(numdecks)

    def setupDeck(self, numdecks=6):
        self.cards = []
        self.decksize = numdecks * 52
        for i in range(numdecks):
            for suit in ['Club', 'Spade', 'Heart', 'Diamond']:
                self.cards.append(Card(suit, 'A'))
                for i in range(2, 10):
                    self.cards.append(Card(suit, i))
                self.cards.append(Card(suit, 'T'))
                self.cards.append(Card(suit,'J'))
                self.cards.append(Card(suit,'Q'))
                self.cards.append(Card(suit,'K'))
        
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def nextCard(self):
        return self.cards.pop(0)
    
    def copy(self):
        d = Deck()
        d.cards = self.cards.copy()
        return d

    def __str__(self):
        for card in self.cards:
            print(card.char, 'of', card.suit)
        return ""
