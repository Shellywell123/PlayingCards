from blackjack import *

balance = 1000
pot = 0

def showbets():
    global balance
    global pot
    print ' YOUR BALANCE    THE POT'
    show_chips([balance,pot])

def buyin(bet):
    global balance
    global pot
    print balance
    balance = balance - bet
    pot = bet*2

def push():
    global pot
    global balance
    balance = balance + pot/2
    pot = 0

def lose():
    global pot
    global balance
    pot = 0

def win():
    global pot
    global balance
    balance = balance+pot
    pot = 0

def raisee(bet):
    global pot
    global balance
    balance = balance-bet
    pot = pot + bet*2


def chipsci(price):
    price = str(price)

    LE = card_back+'#'
    RE = '# '+white

    L = card_back+'#'+redcard
    R = card_back+'#'+white

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