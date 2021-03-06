from deck import *

def exit_process():
    from accounts import who_am_i,refresh_account,leaderboard
    print ('goodbye {}...'.format(who_am_i()))
    refresh_account()
    leaderboard()
    exit(0)

def suited_deck():
    deck = new_deck()
    return deck

def numerical_deck():
    """half numerical atm, but only needed from split checking"""
    deck = new_deck()
    deck = riffle(deck)
    return deck

def new_shuffled_deck():
    #make a deck
    deck = new_deck()

    #shuffle deck
    #show_deck(deck)

    deck = riffle(deck)
    shuffle_comp(deck)
    shuffle_comp(deck)
    deck = riffle(deck)
    shuffle_comp(deck)
    shuffle_comp(deck)
    
    #show_deck(deck)
    #show_backs()
    return deck

def games():
    game = raw_input_bens('\nWhat do you want to play?\n - Blackjack "b"\n - Texas-Holdem "t"\n')
    if game == 'blackjack' or game=='b':
        from games.blackjack import new_shuffled_deck,blackjack,exit_process
        deck=new_shuffled_deck()
        #deck = numerical_deck()
        blackjack(deck)
    if game == 'texas-holdem'or game=='t':
        from games.texas_holdem import new_shuffled_deck,texas_holdem,exit_process
        deck=new_shuffled_deck()
        #deck = new_deck()
        texas_holdem(deck)
    if game == 'exit':
        exit_process()

def suit_line():
    for n in range(10):
        for suit in suits:
            print (suit, end=" ")
    print (white)

def intro():
    suit_line()
    print (greentable+"                      WeLcOmE 2 bEn'S cAsIn0 !                                  "+white)
    suit_line()

def raw_input_bens(str):
    opt = input(output_colour+str+input_colour)
    print (white,)
    return opt

def general_help():
    print (green+''' General
 ------------------------
 - "quit" = exit to games menu
 - "exit" = leave casino
 '''+white)

def default_options(opt):
    if str(opt) =='exit':
        exit_process()

    if str(opt) == 'help':
        from betting import betting_help
        from games.blackjack import blackjack_help
        print (green+'''\nHelp Screen
-------------------------'''+white)
        general_help()
        betting_help()     
        blackjack_help()

    if str(opt) == 'quit':
        from accounts import refresh_account
        refresh_account()
        games()

def clear():
    print(chr(27) + "[2J")