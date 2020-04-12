# -*- coding: utf-8 -*-
#from games.blackjack import *
from deck import *
from stats import *
from general.colours import *
from general.general import *

balance = 1000
pot = 0
last_bet = 0

def set_balance(n):
    global balance
    balance = n

def ret_balance():
    global balance
    return balance

def ret_prev_bet():
    global last_bet
    return last_bet

def betting_help():
    print green+''' Betting
 ------------------------
 - "a" = allin
 - "h" = bet half of balance
 - number = bet $number
    '''+white

def betting_opts():
    prev_bet =  ret_prev_bet()
    balance = ret_balance()

    if prev_bet>0:
        prev_bet_str = "\nPress enter to bet "+input_colour+"$"+str(prev_bet)+output_colour+" again."
    else:
        prev_bet_str = ''
    bi = raw_input_bens("How much do you want to buy in?"+prev_bet_str+input_colour+"\n$")
    default_options(bi)    
    if bi == '':
        bi = prev_bet
    if bi == 'h':
        bi = balance/2.
    if bi == 'a':
        bi = balance
    try:
        bi = int(bi)
    except:
        print red+'"'+str(bi)+'" invalid input please use integer amount\n'+white
        return False
    if bi <=0:
        print red+'"'+str(bi)+'" invalid input please use postive amount\n'+white
        return False
    if bi>balance:
        print red+'"'+str(bi)+'"is more money than you have! ($'+str(balance)+'). Place a lower bet'+white
        return False
    else:
        return bi


def showbets():
    global balance
    global pot
    print ' YOUR BALANCE    THE POT'
    show_chips([balance,pot])

def buyin(bet):
    global balance
    global last_bet
    global pot
    print balance
    if bet>balance:
        '"'+str(bet)+'"is more money than you have! ($'+str(balance)+'). Place a lower bet'+white
    balance = balance - bet
    pot = pot+bet*2
    last_bet = bet
    save_bet(bet)

def push():
    pass
    #global pot
    #global balance
    #balance = balance + pot/2
    #save_bal(balance)
    #pot = 0

def lose():
    global pot
    global balance
    save_bal(balance)
    pot = 0

def win():
    global pot
    global balance
    balance = balance+pot
    save_bal(balance)
    pot = 0

def raisee(bet):
    global pot
    global balance
    if bet>balance:
        print 'you dont have enough money'
        return False
    else:
        balance = balance-bet
        pot = pot + bet*2

        save_bet(bet)
        return True

def broke_check():
    global balance

    if balance <= 0:
        return True
    else:
        return False

def chipsci(price,bg=white):
    price = str(price)

    LE = card_back+'#'
    RE = '# '+bg

    L = card_back+'#'+redcard
    R = card_back+'#'+bg

    if len(price) == 1:
        a = white+' '
        b = ' '
        c = ' '
        d = '$'
        e = price
        f = ' '
        g = ' '
        h = ' '+redcard

    if len(price) == 2:
        a = white+' '
        b = ' '
        c = '$'
        d = price[0]
        e = price[1]
        f = ' '
        g = ' '
        h = ' '+redcard

    if len(price) == 3:
        a = white+' '
        b = ' '
        c = '$'
        d = price[0]
        e = price[1]
        f = price[2]
        g = ' '
        h = ' '+redcard

    if len(price) == 4:
        a = white+' '
        b = '$'
        c = price[0]
        d = price[1]
        e = price[2]
        f = price[3]
        g = ' '
        h = ' '+redcard

    if len(price) == 5:
        a = white+' '
        b = '$'
        c = price[0]
        d = price[1]
        e = price[2]
        f = price[3]
        g = price[4]
        h = ' '+redcard

    if len(price) == 6:
        a = white+'$'
        b = price[0]
        c = price[1]
        d = price[2]
        e = price[3]
        f = price[4]
        g = price[5]
        h = ' '+redcard

    if len(price) == 7:
        a = white+'$'
        b = price[0]
        c = price[1]
        d = price[2]
        e = price[3]
        f = price[4]
        g = price[5]
        h = price[6]+redcard

    chip = """   {} # # {}  
  {} ------ {} 
 {} ======== {}
 {} {}{}{}{}{}{}{}{} {}
 {} ======== {}
  {} ------ {} 
   {} # # {}  """.format(LE,RE,L,R,L,R,L,a,b,c,d,e,f,g,h,R,L,R,L,R,LE,RE)

    return chip

def show_chips(chipsmessy):

    chips = []

    for chip in chipsmessy:
        chips.append(chipsci(chip))

    for n in range(7):
        for chip in chips:
            lines = chip.split('\n')
            print lines[n],
        print '\n',

def show_hand_bet(messyhand,chip,bg=white):
    
    hand = []
    
    global balance
    global pot
    global balance
    global pot
    if chip == 'dealers':
        chip = pot
        hand.append(bg+'             \n'*2+'     POT     \n'+chipsci(chip,bg=bg))
    else:
        chip=balance
        hand.append(bg+'             \n'*2+' YOUR BALANCE\n'+chipsci(chip,bg=bg))

    for card in messyhand:
        num,suit=getinfo(card)
        hand.append(cardsci(num,suit,bg=bg))

    print bg
    for n in range(10):
        for card in hand:
            lines = card.split('\n')
            print lines[n],
        print '\n',

def show_hands_bet(messyhand1,messyhand2,chip,bg=white):

    hand1 = []
    hand2 = []

    global balance
    global pot
    global balance
    global pot

    if chip == 'dealers':
        chip = pot
        hand1.append(bg+'             \n'*2+'     POT     \n'+chipsci(chip,bg=bg))
    else:
        chip=balance
        hand1.append(bg+'             \n'*2+' YOUR BALANCE\n'+chipsci(chip,bg=bg))
        hand2.append(bg+'             \n'*2+' YOUR BALANCE\n'+chipsci(chip,bg=bg))

    for card in messyhand1:
        num,suit=getinfo(card)
        hand1.append(cardsci(num,suit,bg=bg))

    for card in messyhand1:
        num,suit=getinfo(card)
        hand2.append(cardsci(num,suit,bg=bg))

    print bg
    if len(hand1)==len(hand2):
        for n in range(10):
            for card in hand1:
                lines = card.split('\n')
                print lines[n],
            print '\n',

            for card in hand2:
                lines = card.split('\n')
                print lines[n],
            print '\n',
    else:
        print 'hands are of diff size'

def show_split_hand_bet(hand1,hand2,bg1,bg2):
    global balance
    chip = bg1+'             \n'*2+' YOUR BALANCE \n'+chipsci(balance,bg=bg1)
    hand1 = [str(chip)]+hand1

    for card in hand1:
        lines = card.split('\n')
        print len(lines)

    show_hands(hand1,hand2,bg1=bg1,bg2=bg2)


def show_half_hand_bet(messyhand,chip,bg=white):
    hand = []
    global balance
    global pot
    if chip == 'dealers':
        chip = pot
        hand.append(bg+'             \n'*2+'     POT     \n'+chipsci(chip,bg=bg))
    else:
        chip=balance
        hand.append(bg+'             \n'*2+' YOUR BALANCE \n'+chipsci(chip,bg=bg))

    for card in messyhand:
        num,suit=getinfo(card)
        hand.append(cardsci(num,suit,bg=bg))

    hand = hand[:-1] + [cardsci('#','#',bg=bg)]

    print bg
    for n in range(10):
        for card in hand:
            lines = card.split('\n')
            print lines[n],
        print '\n',

def show_blind_hand_bet(messyhand,chip,bg=white):
    hand = []
    global balance
    global pot
    if chip == 'dealers':
        chip = pot
        hand.append(bg+'             \n'*2+'     POT     \n'+chipsci(chip,bg=bg))
    if chip == 'cpus':
        chip = 1000 #cpu money tbs
        hand.append(bg+'             \n'*2+'     CPU     \n'+chipsci(chip,bg=bg))

    else:
        chip=balance
        hand.append(bg+'             \n'*2+' YOUR BALANCE \n'+chipsci(chip,bg=bg))

    hand.append(cardsci('#','#',bg=bg))
    hand.append(cardsci('#','#',bg=bg))

    print bg
    for n in range(10):
        for card in hand:
            lines = card.split('\n')
            print lines[n],
        print '\n',