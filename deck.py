# -*- coding: utf-8 -*-
from stats import *
from general.colours import *

#python 2
# spades = blackcard+'\xe2\x99\xa0'
# diamonds = redcard+'\xe2\x99\xa6'
# hearts =redcard+'\xe2\x99\xa5'
# clubs = blackcard+'\xe2\x99\xa3'

#pythn3 
spades = blackcard+'♠'
diamonds = redcard+'♦'
hearts =redcard+ '♥'
clubs = blackcard+'♣'

suits =   [spades,clubs,hearts,diamonds]
numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

count = 0
    
def shuffle_comp(deck):
    from random import shuffle
    deck = shuffle(deck)
    return deck

def new_deck():
    deck = []
    
    for suit in suits:
        for number in numbers:
            deck.append(number+suit)

    return deck

def split(deck):
    split = len(deck)//2
    return deck[:split], deck[split:]

def riffle(deck):
    top,bottom = split(deck)
    riffled = []

    for n in range(len(top)):
        riffled.append(top[n])
        riffled.append(bottom[n])
    return riffled

def fan(deck):
    for card in deck:
        print (card)
    
def draw(n,deck):
    hand = deck[:n]
    deck2 = deck[n:]+deck[:n]
    increase_drawncount(n)
    return deck2,hand


def cardsci(num,suit,bg=white):
    if not num=='10':
        numtop = num+' '
        numbot = ' '+num
    else:
        numtop = num
        numbot = num
     
    a=blackcard+' '
    b=blackcard+' '
    c=blackcard+' '
    d=blackcard+' '
    e=blackcard+' '
    f=blackcard+' '
    g=blackcard+' '
    h=blackcard+' '
    i=blackcard+' '
    k=blackcard+' '
    l=blackcard+' '
    m=blackcard+' '
    n=blackcard+' '
    o=blackcard+' '
    p=blackcard+' '
    q=blackcard+' '
    r=blackcard+' '
    s=blackcard+' '
    t=blackcard+' '
    u=blackcard+' '
    v=blackcard+' '

    if num == 'temp':
        a='a'
        b='b'
        c='c'
        d='d'
        e='e'
        f='f'
        g='g'
        h='h'
        i='i'
        k='k'
        l='l'
        m='m'
        n='n'
        o='o'
        p='p'
        q='q'
        r='r'
        s='s'
        t='t'
        u='u'
        v='v'

    if num == 'A':
        l=suit

    if num == '2':
        e=suit
        r=suit

    if num =='3':
        e=suit
        l=suit
        r=suit

    if num =='4':
        d=suit
        f=suit
        q=suit
        s=suit

    if num == '5':
        d=suit
        f=suit
        l=suit
        q=suit
        s=suit

    if num == '6':
        d=suit
        f=suit
        k=suit
        m=suit
        q=suit
        s=suit

    if num =='7':
        d=suit
        f=suit
        h=suit
        k=suit
        m=suit
        q=suit
        s=suit

    if num == '8':
        d=suit
        f=suit
        h=suit
        k=suit
        m=suit
        o=suit
        q=suit
        s=suit

    if num == '9':
        a=suit
        c=suit
        g=suit
        i=suit
        l=suit
        n=suit
        p=suit
        t=suit
        v=suit

    if num == '10':
        a=suit
        c=suit
        e=suit
        g=suit
        i=suit
        n=suit
        p=suit
        r=suit
        t=suit
        v=suit

    if num == 'J':
        
        d=suit
        e=suit
        f=suit
        h=suit
        l=suit
        o=suit
        q=suit
        r=suit

    if num == 'Q':
        d=suit
        e=suit
        f=suit
        i=suit
        g=suit
        m=suit
        k=suit
        n=suit
        o=suit
        s=suit

    if num == 'K':
        d=suit
        i=suit
        g=suit
        l=suit
        k=suit
        n=suit
        o=suit
        q=suit
        s=suit


    L = blackcard
    R = bg

    _cardsci = """
{}{}         {}
{}   {} {} {}   {}
{}   {} {} {}   {}
{}   {} {} {}   {}
{}   {} {} {}   {}
{}   {} {} {}   {}
{}   {} {} {}   {}
{}   {} {} {}   {}
{}         {}{}""".format(
            L,numtop,R,
            L,a,b,c,R,
            L,d,e,f,R,
            L,g,h,i,R,
            L,k,l,m,R,
            L,n,o,p,R,
            L,q,r,s,R,
            L,t,u,v,R,
            L,numbot,R)

    if num == '#':
        _cardsci = bg+'\n'+((redcard+(' '*11))+bg)+('\n' +((redcard+' '+card_back+('#'*9))+redcard+' '+bg))*7 +'\n'+((redcard+(' '*11))+bg)

    return _cardsci

def show_backs():
    hand = []
    for n in range(4):
        hand.append(cardsci('#','#'))

    for n in range(10):
        for card in hand:
            lines = card.split('\n')
            print (lines[n],)
        print ('\n',)


def show_deck(deck):
   
    for n in range(0,len(deck),4):
        hand = []
                    
        hand.append(deck[n])
        hand.append(deck[n+1])
        hand.append(deck[n+2])
        hand.append(deck[n+3])
        show_hand(hand)

def show_deck_flat(deck):
   
    for n in range(0,len(deck),13):
        hand = []
                    
        hand.append(deck[n])
        hand.append(deck[n+1])
        hand.append(deck[n+2])
        hand.append(deck[n+3])
        hand.append(deck[n+4])
        hand.append(deck[n+5])
        hand.append(deck[n+6])
        hand.append(deck[n+7])
        hand.append(deck[n+8])
        hand.append(deck[n+9])
        hand.append(deck[n+10])
        hand.append(deck[n+11])
        hand.append(deck[n+12])


        show_hand(hand)

def show_hand(messyhand,bg=white):
    hand = []

    for card in messyhand:
        num,suit=getinfo(card)
        hand.append(cardsci(num,suit,bg=bg))

    print (bg)
    string = ''
    for n in range(10):
        for card in hand:
            lines = card.split('\n')
            print (lines[n],)
            string=string+lines[n]
        print ('\n',)
        string=string+'\n'
    return string

def show_hands(messyhand1,messyhand2,bg1=white,bg2=white):
    hand1 = []
    hand2 = []

    for card in messyhand1:
        num,suit=getinfo(card)
        hand1.append(cardsci(num,suit,bg=bg1))

    for card in messyhand2:
        num,suit=getinfo(card)
        hand2.append(cardsci(num,suit,bg=bg2))

    string1 = ''
    for n in range(10):
        for card in hand1:
            lines = card.split('\n')
         #   print lines[n],
            string1=string1+lines[n]+' '
     #   print '\n',
        string1=string1+'\n'

    string2 = ''
    for n in range(10):
        for card in hand2:
            lines = card.split('\n')
         #   print lines[n],
            string2=string2+lines[n]+' '
       # print '\n',
        string2=string2+'\n'

    string_final = ''
    for n in range(10):
        for string in [string1,string2]:
            lines = string.split('\n')
            print (lines[n],' '*5,)
            string_final=string_final+lines[n]
        print ('\n',)
        string_final=string_final+'\n'

    return string1,string2,string_final

def show_half_hand(messyhand,bg=white):
    hand = []

    for card in messyhand:
        num,suit=getinfo(card)
        hand.append(cardsci(num,suit,bg=bg))

    hand = hand[:-1] + [cardsci('#','#',bg=bg)]

    print (bg)
    for n in range(10):
        for card in hand:
            lines = card.split('\n')
            print (lines[n],)
        print ('\n',)

def getinfo(card):
    num = card.split('\x1b')[0]
    suit = '\x1b'+card.split('\x1b')[1]

   # print num,suit
    return num,suit

def split_hand(hand):
    hand1 = [hand[0]]
    hand2 = [hand[1]]
    return hand1,hand2


