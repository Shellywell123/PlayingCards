from deck import *
from games import *

deck = new_deck()
show_deck(deck)
deck = riffle(deck)
shuffle(deck)
show_backs()
blackjack(deck)