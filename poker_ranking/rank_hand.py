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

def compare_hands(hand1,hand2):
  """
  """
  hand1matrix = hand_encoder(hand1)
  hand1scores = pipeline.evaluate(hand1matrix)

  hand2matrix = hand_encoder(hand2)
  hand2scores = pipeline.evaluate(hand2matrix)

  for i in range(0,2):
    if hand1scores[i] > hand2scores:
      return '1'
      #then hand 1 wins
    if hand2scores[i] > hand1scores:
      return '2'
      #then hand 2 wins
    if hand1scores[i] == hand2scores:
      #then check next layer in or for draw
      if i == 2:
        #then hands draw

