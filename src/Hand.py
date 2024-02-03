

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def card_value(self, card):
        if card.value == 'J':
            return 11
        elif card.value == 'Q':
            return 12
        elif card.value == 'K':
            return 13
        elif card.value == 'A':
            return 14
        else:
            return int(card.value)
        
    def calculate_points(self):
        #summa av alla values i cards
        points = 0
        for card in self.cards:
            points += self.card_value(card) 

        if points > 21 and self.has_ace():
            points -= 13

        return points

        
    def has_ace(self):
        #returnera true om det finns ett ess i handen
        #annars false
        for card in self.cards:
            if card.value == 'A':
                return True
            
    def getCards(self):
        return [str(card) for card in self.cards]
    