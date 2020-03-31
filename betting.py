from blackjack import *

balance = 1000
pot = 0

def showbets():
    global balance
    global pot
    print 'YOUR BALANCE = $'+str(balance)
    print 'THE POT = $'+str(pot)

def buyin(bet):
    global balance
    global pot
    print balance
    balance = balance - bet
    pot = bet*2
    showbets()

def push():
    global pot
    global balance
    balance = balance + pot/2
    pot = 0
    showbets()

def lose():
    global pot
    global balance
    pot = 0
    showbets()

def win():
    global pot
    global balance
    balance = balance+pot
    pot = 0
    showbets()

def raisee(bet):
    global pot
    global balance
    balance = balance-bet
    pot = pot + bet*2
    showbets()