
from Deck import Deck
from Player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player()
        self.player2 = Player()

    def dealFirstCards(self):
        for i in range(0,1):
            self.player1.hand.add_card(self.deck.deal_card())
            self.player2.hand.add_card(self.deck.deal_card())


    def checkDeckEmpty(self):
        if len(self.deck) == 0:
            self.deck = Deck()

    def cardToString(self, array):
        result_string = ', '.join(array)
        return result_string

    def isGameOver(self, value):
        if value > 21:
            return True
        else:
            return False

    def play(self):
        
        print("Välkommen till TjugoEtt för två spelare!")
        self.dealFirstCards()
        
        while True:
            print("Spelare 1 har", self.cardToString(self.player1.hand.getCards()), "och har", self.player1.hand.calculate_points(), "poäng!")
            print("Spelare 2 har", self.cardToString(self.player2.hand.getCards()), "och har", self.player2.hand.calculate_points(), "poäng!\n")

            while True:
                ans = input("Spelare 1, vill du ha ett kort till? y/n: ")
                if ans == "y":
                    self.player1.hand.add_card(self.deck.deal_card())
                    print("Du har",self.cardToString(self.player1.hand.getCards()),"och har",self.player1.hand.calculate_points(), "poäng!\n")
                    if(self.isGameOver(self.player1.hand.calculate_points())):
                        print("Du förlorade!!!!!")
                        break

                if ans == "n":
                    break
        
            
            while True:
                ans = input("Spelare 2, vill du ha ett kort till? y/n: ")
                if ans == "y":
                    self.player2.hand.add_card(self.deck.deal_card())
                    print("Du har",self.cardToString(self.player2.hand.getCards()),"och har",self.player2.hand.calculate_points(), "poäng!\n")
                    if(self.isGameOver(self.player2.hand.calculate_points())):
                        print("Du förlorade!!!!!")
                        break
            
                if ans == "n":
                    break






if __name__ == '__main__':
    game = Game()
    game.play()



'''
    def checkDeckEmpty(self):
        if len(self.deck) == 0:
            self.deck = Deck()

    def cardToString(self, array):
        result_string = ', '.join(array)
        return result_string

    def play(self):
        
        print("Välkommen till TjugoEtt för två spelare!")
        self.dealFirstCards()
        
        while True:
            print("Spelare 1 har", self.cardToString(self.player1.hand.getCards()), "och har", self.player1.hand.calculate_points(), "poäng!")
            print("Spelare 2 har", self.cardToString(self.player2.hand.getCards()), "och har", self.player2.hand.calculate_points(), "poäng!\n")

            ans = input("Spelare 1, vill du ha ett kort till? y/n: ")
            if ans == "y":
                self.player1.hand.add_card(self.deck.deal_card())
                print("Du har",self.cardToString(self.player1.hand.getCards()),"och har",self.player1.hand.calculate_points(), "poäng!\n")
            if ans == "n":
                pass

            ans = input("Spelare 2, vill du ha ett kort till? y/n: ")
            if ans == "y":
                self.player2.hand.add_card(self.deck.deal_card())
                print("Du har",self.cardToString(self.player2.hand.getCards()),"och har",self.player2.hand.calculate_points(), "poäng!\n")
            if ans == "n":
                pass

'''