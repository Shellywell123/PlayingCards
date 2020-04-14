from deck import *
from betting import *
from general.console import *
from general.general import *
from general.colours import *
from accounts import *
from collections import Counter

def show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=False):
    
    width,hight = terminal_size()
    print'-'*width
   # count = counting([dealers_hand[0]]+hand)
    print'-'*width

    print '\n'+bluetable+"DEALER'S HAND"
    show_hand_bet(dealers_hand,'dealers',bg=bluetable)
    if blind==True:
        print '\n'+greentable+"YOUR HAND                                         CPU's HAND"
        show_hands_bet(hand,cpu_hand,bg=greentable,blind=True)
    else:
        print '\n'+greentable+"YOUR HAND                                         CPU's HAND"
        show_hands_bet(hand,cpu_hand,bg=greentable)
    print white
    
 #   showbets()

def check_dups(listofthings):
    d =dict(Counter(listofthings))         

    dupsdata = []                                                                              
    for thing in d:
        numofdups=d[thing]
        #print thing,numofdups
        dupsdata.append([thing,numofdups])

    return dupsdata

def check_pair_trip_quad(nums):
    cd = check_dups(nums)
    for element in cd:
        if element[1] == 2:
            print 'you have a PAIR of '+str(element[0])+"'s"
        if element[1] == 3:
            print 'you have a  TRIPs of '+(element[0])+"'s"
        if element[1] == 4:
            print 'you have a QUADs of '+str(element[0])+"'s"

def check_flush(suits):
    cd=check_dups(suits)

    for element in cd:
        if element[1] == 5:
            print str(element[0])+white+'FLUSH'

def check_straight(nums):
    pass

def check_card_high(nums):
    pass

def eval_hand(hand,table_cards):

    hand = hand + table_cards

    nums = []
    suits = []

    for card in hand:
        num,suit = getinfo(card)
        nums.append(num)
        suits.append(suit)

    check_flush(suits)
    check_pair_trip_quad(nums)
   # if len(table_cards)==5:
   #     print '5'

    #if len(table_cards)==4:
     #   print '4'

    #if len(table_cards)==3:
    #    print '3'


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
        print red+'"'+str(bi)+'" invalid input please use integer amount\n'+white
        texas_holdem(deck)
    if bi <=0:
        print red+'"'+str(bi)+'" invalid input please use postive amount\n'+white
        texas_holdem(deck)
    if bi>balance:
        print red+'"'+str(bi)+'"is more money than you have! ($'+str(balance)+'). Place a lower bet'+white
        texas_holdem(deck)
    
        
    buyin(bi)
    dealers_val=0
    dealers_val_blind=0
    val=0
    
    def ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val):
        if len(dealers_hand)==5:
            show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=False)
            print white+'end of this hand'
            
            eval_hand(hand,dealers_hand)
            reverse_bet()
            deck = shuffle_comp(deck)
            texas_holdem(deck)
        else:
            show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=True)
            eval_hand(hand,dealers_hand)
            optstring = "Call("+input_colour+"c"+output_colour+") Raise("+input_colour+"r"+output_colour+"), Check("+input_colour+"ch"+output_colour+") or Fold("+input_colour+"f"+output_colour+")?\n"
            opt = raw_input_bens(optstring)
            default_options(opt)
            if opt=='f':
                print 'You Fold'
                reverse_bet()
                texas_holdem(deck)
            if opt =='r':
                print 'You raised'
                ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val)
            if opt =='c':
                print 'You Called'
                ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val)
            if opt=='ch' or opt=='':
                print 'You Check'
                deck,river = draw(1,deck)
                dealers_hand = dealers_hand + river
                show_table(dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val,blind=False)
                ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val)

    ask(deck,dealers_hand,hand,cpu_hand,dealers_val,dealers_val_blind,val)
    