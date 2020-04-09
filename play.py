from deck import *
from accounts import *
from general import *

#make a deck
deck = new_deck()

#shuffle deck
#show_deck(deck)
deck = riffle(deck)
shuffle(deck)
shuffle(deck)
deck = riffle(deck)
shuffle(deck)
shuffle(deck)
#show_deck(deck)
#show_backs()

#initiate games

intro()
user_query()
games(deck)