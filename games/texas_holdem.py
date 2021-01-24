from deck import *
from betting import *
from general.console import *
from general.general import *
from general.colours import *
from accounts import *
from collections import Counter

from games.poker_ranking.encoder import hand_encoder
from games.poker_ranking.scorepipeline import *

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

def show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=False):
    
    width,hight = terminal_size()
    print('-'*width)
   # count = counting([dealers_hand[0]]+hand)
    print('-'*width)

    print ('\n'+bluetable+"DEALER'S HAND")
    show_hand_bet(dealers_hand,'dealers',bg=bluetable)
    if blind==True:
        print ('\n'+greentable+"YOUR HAND                                         CPU's HAND")
        show_hands_bet(hand,cpu_hand,bg=greentable,blind=True)
    else:
        print ('\n'+greentable+"YOUR HAND                                         CPU's HAND")
        show_hands_bet(hand,cpu_hand,bg=greentable)
    print (white)
    
#  #   showbets()

# def check_dups(listofthings):
#     d =dict(Counter(listofthings))         

#     dupsdata = []                                                                              
#     for thing in d:
#         numofdups=d[thing]
#         #print thing,numofdups
#         dupsdata.append([thing,numofdups])

#     return dupsdata

# def evaluate_num(num):
#     if num == 'A':
#         return 14

#     if num  =='J':
#         return 11

#     if num  =='Q':
#         return 12

#     if num  =='K':
#         return 13

#     if num in ['2','3','4','5','6','7','8','9','10']:
#         return int(num)

# def val_order(hand):
    
#     values = []

#     for card in hand:
#         val = evaluate_num(card)
#         values.append(int(val))

#     sorted_ = [x for _,x in sorted(zip(values,hand))]
#     sorted_ = list(reversed(sorted_))
#     return sorted_

# def check_pair_trip_quad(nums):
#     """
#     high card/s after dups need to do
#     need to make a funt that takes n cards and returns list of value
#     so can return num of high cards to fil hand
#     """

#     cd = check_dups(nums)
#     best_pair_hand = []

#     fullhouse = []
#     high_card = val_order(nums)
#     print (high_card)

#     for element in cd:

#         if element[1] == 2:
#             print ('PAIR of '+str(element[0])+"'s")
#             fullhouse.append(element[0])
#             fullhouse.append(element[0])

#             best_pair_hand.append(element[0])
#             best_pair_hand.append(element[0])

#         if element[1] == 3:
#             print ('TRIPs of '+(element[0])+"'s")
#             fullhouse.append(element[0])
#             fullhouse.append(element[0])
#             fullhouse.append(element[0])

#             best_pair_hand.append(element[0])
#             best_pair_hand.append(element[0])
#             best_pair_hand.append(element[0])

#         if element[1] == 4:
#             print ('QUADs of '+str(element[0])+"'s")
#             best_pair_hand.append(element[0])
#             best_pair_hand.append(element[0])
#             best_pair_hand.append(element[0])
#             best_pair_hand.append(element[0])
#             best_pair_hand = best_pair_hand + high_card[:1]

#     if len(best_pair_hand) == 0:
#         best_pair_hand = best_pair_hand + high_card[:5]

#     if len(best_pair_hand) == 4:
#         best_pair_hand = best_pair_hand + high_card[:1]

#     if len(best_pair_hand) == 3:
#         best_pair_hand = best_pair_hand + high_card[:2]

#     if len(best_pair_hand) == 2:
#         best_pair_hand = best_pair_hand + high_card[:3]

#     if len(fullhouse) == 5:
#         print ('fullhouse!')
#         best_pair_hand = fullhouse

#     print (best_pair_hand)

# def check_flush(suits):
#     cd=check_dups(suits)

#     for element in cd:
#         if element[1] == 5:
#             print (str(element[0])+white+'FLUSH')

# def check_straight(nums):
#     pass

# def check_card_high(nums):
#     pass

# def eval_hand(hand,table_cards):
#     """
#     finds best five cards for a given players hand
#     """

#     hand = hand + table_cards

#     nums = []
#     suits = [] 

#     for card in hand:
#         num,suit = getinfo(card)
#         nums.append(num)
#         suits.append(suit)

#     check_flush(suits)
#     check_pair_trip_quad(nums)
#    # if len(table_cards)==5:
#    #     print '5'

#     #if len(table_cards)==4:
#      #   print '4'

#     #if len(table_cards)==3:
#     #    print '3'

# def compare_hands(my_hand, cpu_hand):
#     """
#     royal flush
#     straight flush
#     quads
#     fullhouse
#     fluah
#     straight
#     trips
#     2 pair
#     pair
#     high card
#     """


def evaluate_hand(hand):
    """
    """
    matrix = hand_encoder(hand)
    #   print (matrix)

    scores = pipeline.evaluate(matrix)
    #  print(scores)


    #   print(list(map(hex, scores)))
    return scores[0]

def whats_in_this_hand(hand):
    """
    gives poker desciption of card combinations in the hand supplied
    """
    val = evaluate_hand(hand)

    klasses = [    
    'High Card',
    'Pair of',
    'Two Pair',
    'Three of a Kind',
    'straight',
    'Flush',
    'Fullhouse',
    'Four of a Kind',
    'Straight-Flush',
    'Royal-Flush'
    ]

    cards = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A']

    i,j,k = val

    print(val)

    extra = ''

    if i == 1:
        extra = "'s"

    if i == 2:
        extra = "'s & "+ cards[k] +"'s"

    # elif:
    #     extra = ' high.'

    return klasses[i] + ' ' + cards[j] + extra




def compare_hands(hand1,hand2):
  """
  Evaluates 2 hands and gives wininng hand
  """
  hand1matrix = hand_encoder(hand1)
  hand1scores = pipeline.evaluate(hand1matrix)

  hand2matrix = hand_encoder(hand2)
  hand2scores = pipeline.evaluate(hand2matrix)

  print(hand1scores[0],'vs',hand2scores[0])
  for i in range(0,2):
    if hand1scores[i] > hand2scores[i]:
      return '1'
      #then hand 1 wins
    if hand2scores[i] > hand1scores[i]:
      return '2'
      #then hand 2 wins
    if hand1scores[i] == hand2scores[i] and i==2:
      return 'd'

def texas_holdem(deck):

    deck,dealers_hand = draw(3,deck)
    deck,hand = draw(2,deck)
    deck,cpu_hand = draw(2,deck)
    
    balance = ret_balance()
   # print 'ret bal='+str(balance)

    showbets()
    prev_bet =  ret_prev_bet()
    if prev_bet>0:
        prev_bet_str = "\nPress enter to bet "+input_colour+"$"+str(prev_bet)+output_colour+" again."
    else:
        prev_bet_str = ''
    bi = raw_input_bens("How much do you want to buy in?\n(NB every hit will cost you this amount again)"+prev_bet_str+input_colour+"\n$")
    
    default_options(bi) 
    if bi == '':
        bi = prev_bet
    try:
        bi = int(bi)
    except:
        print (red+'"'+str(bi)+'" invalid input please use integer amount\n'+white)
        texas_holdem(deck)
    if bi <=0:
        print (red+'"'+str(bi)+'" invalid input please use postive amount\n'+white)
        texas_holdem(deck)
    if bi>balance:
        print (red+'"'+str(bi)+'"is more money than you have! ($'+str(balance)+'). Place a lower bet'+white)
        texas_holdem(deck)
    
        
    buyin(bi)
    dealers_val=0
    dealers_val_blind=0
    val=0
    

    def player_opts(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,show_cpu):
        """
        """
        show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=True)
        print('You have a',whats_in_this_hand(hand+dealers_hand))
        optstring = "Check/Call("+input_colour+"c"+output_colour+") Raise("+input_colour+"r"+output_colour+") or Fold("+input_colour+"f"+output_colour+")?\n"
        opt = raw_input_bens(optstring)
        default_options(opt)
        if opt=='f':
            print ('You Fold')
            reverse_bet()
            texas_holdem(deck)
        if opt =='r':
            print ('You raised')
        #     ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val)
        # if opt =='c':
        #     print ('You Called')
        #     ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val)
        if opt=='c' or opt=='':
            print ('You Check/called')
            if show_cpu == False:
                deck,river = draw(1,deck)
                dealers_hand = dealers_hand + river
          #  show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=False)
            ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,show_cpu)


    show_cpu = False

    def ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,show_cpu):
        if len(dealers_hand)==5:
            if show_cpu == False:

            # # if cpu cards not show give one more orund of betting then show cards
              
            # if cpu_blind == True:
                show_cpu = True
                player_opts(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,show_cpu)

            # # if no more betting evaluate hands and start again
            if show_cpu == True:

                show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=False)
                print (white+'end of this hand')
                
                #eval_hand(hand,dealers_hand)
                outcome= compare_hands(hand+dealers_hand,cpu_hand+dealers_hand)
                print(outcome)

                if outcome == '1':
                    print('you win')
                    print('you have ',whats_in_this_hand(hand+dealers_hand))

                if outcome == '2':
                    print('you lose')
                    print('cpu has ',whats_in_this_hand(cpu_hand+dealers_hand))

                if outcome == 'd':
                    print('draw')

                reverse_bet()
                deck = new_shuffled_deck()
                texas_holdem(deck)



        else:
            player_opts(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,show_cpu)
            
    ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,show_cpu)
    