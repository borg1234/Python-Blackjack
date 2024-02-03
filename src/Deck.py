
import random
from Card import Card

class Deck:
    value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    color = ['♥', '♦', '♣', '♠']

    def __init__(self):
        self.cards = []
        for i in self.color:
            for j in self.value:
                self.cards.append(Card(j, i))
        random.shuffle(self.cards)

    def getCards(self):
        x = [str(card) for card in self.cards]
        return x


    def deal_card(self):
        return self.cards.pop(0)
    
    def size(self):
        return len(self.cards)
