import random

class Card:
    def __init__(self, rank = 0, suit = ""):
        if type(rank) == str:
            self.rank = rank.upper()
        else:
            self.rank = rank
        self.suit = suit
    def __str__(self):
        if self.is_blank():
            return "{:>2}{}".format(self.rank,self.suit)
        else:
            return "{:>3s}".format("blk")
    def is_blank(self):
        return self.rank and self.suit

class Deck:
    def __init__(self):
        self.rank = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        self.suit = ["S","H","D","C"]
        self.deck = []
        for rank in self.rank:
            for suit in self.suit:
                self.deck.append(str(rank) + suit)
    def __str__(self):
        self.str_deck = ""
        for index, card in enumerate(self.deck):          
            if index % 12 == 0:
                self.str_deck += "\n"
            self.str_deck += "{:>3s}".format(card) + " "
        return self.str_deck
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop(0)

class PlayingHand:
    def __init__(self):
        self.hand = []
        for hand in range(13):
            self.hand.append("{}".format("blk"))
    def __str__(self):
        return " ".join(self.hand)
    def add_card(self, card):
        for index, slot in enumerate(self.hand):
            if slot == "blk":
                self.hand[index] = card
                break

def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)

def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    PlayingHand.NUMBER_CARDS = 13
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())

def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)

    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)

# The main program starts here
random.seed(10)
test_cards()

deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)

test_hands(deck)
print("The deck after dealing:")
print(deck)