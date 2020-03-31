from deck import *
from blackjack import *

deck = new_deck()
#show_deck(deck)
deck = riffle(deck)
shuffle(deck)
shuffle(deck)
deck = riffle(deck)
shuffle(deck)
shuffle(deck)
#show_deck(deck)
#show_backs()
blackjack(deck)