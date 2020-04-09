from deck import *
from games.blackjack import *
from games.texas_holdem import *
from accounts import *

def games():
    game = raw_input_bens('\nWhat do you want to play?\n - Blackjack "b"\n - Texas-Holdem "t"\n')
    print white,
    if game == 'blackjack' or game=='b':
        blackjack(deck)
    if game == 'texas-holdem'or game=='t':
        texas_holdem(deck)

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
for n in range(10):
    for suit in suits:
        print suit,

print white

user_query()
games()