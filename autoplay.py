
def run(text_input):
    import sys
    import StringIO
    f1 = sys.stdin
    f = StringIO.StringIO(text_input) # <-- HERE
    sys.stdin = f
    f.close()
    sys.stdin = f1

def start(text_input):
    import sys
    import StringIO
    f1 = sys.stdin
    f = StringIO.StringIO(text_input) # <-- HERE
    sys.stdin = f
    import play
    f.close()
    sys.stdin = f1

from deck import *
from games.blackjack import *

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
blackjack_CPU(deck,100)