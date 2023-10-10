import random

class Card(object):
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value
    

    def show(self):
        if self.value == 1:
            self.value = "Ace"
        elif self.value == 11:
            self.value = "Jack"
        elif self.value == 12:
            self.value = "Queen"
        elif self.value == 13:
            self.value = "King"
        return (self.value, "of", self.suit)

class Deck(object):
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        s=["hearts", "spades", "clubs", "diamonds"]
        for i in s:
            for j in range(1, 14):
                self.cards.append(Card(i, j))
    def show(self):
        for i in self.cards:
            print (i.show())
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r=random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def deal(self):
        return self.cards.pop()
class Player(object):
    def __init__(self, name):
        self.name=name
        self.hand=[]
    def draw(self, deck, num):
        for i in range(num):
            card=deck.deal()
            if card:
                self.hand.append(card)
            else:
                print("there is no cards left")
                return False
        return True
    def discard(self):
        self.hand.pop()
    def show_hand(self):
        print(f"{self.name}'s hand is:")
        for card in self.hand:
            print(card.show())

mydeck=Deck()
mydeck.shuffle()
Aaron=Player("Aaron")
Aaron.draw(mydeck, 10)
Aaron.show_hand()