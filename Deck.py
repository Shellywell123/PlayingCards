red = '\033[91m'
yellow ='\033[93m'
blue = '\033[94m'
white='\033[0m'
green='\033[32m'

spades = blue+'\xe2\x99\xa0'+white
diamonds = red+'\xe2\x99\xa6'+white
hearts =red+'\xe2\x99\xa5'+white
clubs = blue+'\xe2\x99\xa3'+white

suits =   [spades,clubs,hearts,diamonds]
numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

count = 0

def shuffle(deck):
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
    for card in deck: print card

    
def draw(n,deck):
    hand = deck[:n]
    deck2 = deck[2:]+deck[:2]
    return deck2,hand


def cardsci(num,suit):
    if not num=='10':
        numtop = num+' '
        numbot = ' '+num
    else:
        numtop = num
        numbot = num
     

    a=' '
    b=' '
    c=' '
    d=' '
    e=' '
    f=' '
    g=' '
    h=' '
    i=' '
    k=' '
    l=' '
    m=' '
    n=' '
    o=' '
    p=' '
    q=' '
    r=' '
    s=' '
    t=' '
    u=' '
    v=' '

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

    if num == '#':
        numtop = '  '
        numbot = '  '
        back=green+'#'+white
        a=back
        b=back
        c=back
        d=back
        e=back
        f=back
        g=back
        h=back
        i=back
        k=back
        l=back
        m=back
        n=back
        o=back
        p=back
        q=back
        r=back
        s=back
        t=back
        u=back
        v=back

    return """
          -------------
         |{}          |
         |    {} {} {}   |
         |    {} {} {}   |
         |    {} {} {}   |
         |    {} {} {}   |
         |    {} {} {}   |
         |    {} {} {}   |
         |    {} {} {}   |
         |          {}|
          -------------
          """.format(numtop,a,b,c,d,e,f,g,h,i,k,l,m,n,o,p,q,r,s,t,u,v,numbot)


def show_deck(deck):
   
    for n in range(0,len(deck),4):
        hand = []
                    
        hand.append(deck[n])
        hand.append(deck[n+1])
        hand.append(deck[n+2])
        hand.append(deck[n+3])

        show_hand(hand)
        
def show_hand(messyhand):
    hand = []

    for card in messyhand:
        num,suit=getinfo(card)
        hand.append(cardsci(num,suit))

    for n in range(13):
        for card in hand:
            lines = card.split('\n')
            print lines[n],
        print '\n',

def getinfo(card):
    num = card.split('\x1b')[0]
    suit = '\x1b'+card.split('\x1b')[1] +white

   # print num,suit
    return num,suit

