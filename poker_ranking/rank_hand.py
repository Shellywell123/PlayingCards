# test

from scorepipeline import *
from encoder import hand_encoder

# instantitate the function pipeline
pipeline = Pipeline(
  royalflush,
  straightflush,
  fourofakind,
  fullhouse,
  flush,
  straight,
  tripples,
  twopair,
  pair,
  highcard
)

royalflush = ['A\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♠',
        'J\x1b[0;30;47m♠',
        'K\x1b[0;30;47m♠',
        'Q\x1b[0;30;47m♠',]

straightflush = ['A\x1b[0;30;47m♠',
        '2\x1b[0;30;47m♠',
        '3\x1b[0;30;47m♠',
        '4\x1b[0;30;47m♠',
        '5\x1b[0;30;47m♠',]

fourofakind = ['2\x1b[0;30;47m♠',
        '2\x1b[0;30;47m♦',
        '2\x1b[0;30;47m♣'
        '10\x1b[0;30;47m♥',
        '10\x1b[0;30;47m♠',]

fullhouse = ['6\x1b[0;30;47m♦',
        '6\x1b[0;30;47m♥',
        '6\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♦',
        '10\x1b[0;30;47m♠',]

flush = ['4\x1b[0;30;47m♠',
        '7\x1b[0;30;47m♠',
        '2\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♠',
        'K\x1b[0;30;47m♠',]

straight = ['A\x1b[0;30;47m♠',
        '2\x1b[0;30;47m♥',
        '3\x1b[0;30;47m♣',
        '4\x1b[0;30;47m♠',
        '5\x1b[0;30;47m♠',]

tripples = ['2\x1b[0;30;47m♥',
        '2\x1b[0;30;47m♦',
        '2\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♥',
        '4\x1b[0;30;47m♠',]

twopair = ['2\x1b[0;30;47m♥',
        '5\x1b[0;30;47m♠',
        '5\x1b[0;30;47m♥',
        '10\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♥',]

pair = ['2\x1b[0;30;47m♠',
        '6\x1b[0;30;47m♠',
        '8\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♥',
        '10\x1b[0;30;47m♠',]

highcard = ['J\x1b[0;30;47m♥',
        '2\x1b[0;30;47m♠',
        '6\x1b[0;30;47m♠',
        '10\x1b[0;30;47m♠',
        '7\x1b[0;30;47m♠',]


tests = [royalflush,straightflush,flush,pair,twopair,highcard,straight,fullhouse,fourofakind,tripples]

for hand in tests:
  matrix = hand_encoder(hand)
  print (matrix)

  scores = pipeline.evaluate(matrix)
  print(scores)

  print(list(map(hex, scores)))