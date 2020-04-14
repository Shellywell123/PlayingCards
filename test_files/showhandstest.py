from deck import *
from betting import *

deck = new_deck()
deck = riffle(deck)
deck,h1 = draw(1,deck)
deck,h2 = draw(1,deck)

show_hand(h1+h2)
show_hands(h1,h2,bg1=bluetable,bg2=greentable)
show_split_hand_bet(h1,h2,bg1=greentable,bg2=greentable)