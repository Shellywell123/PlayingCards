from deck import *

def exit_process():
    from accounts import who_am_i,refresh_account,leaderboard
    print 'goodbye {}...'.format(who_am_i())
    refresh_account()
    leaderboard()
    exit(0)

def new_shuffled_deck():
    #make a deck
    deck = new_deck()

    #shuffle deck
    #show_deck(deck)
    deck = riffle(deck)
    shuffle(deck)
    shuffle(deck)
    deck = riffle(deck)
    shuffle(deck)
    shuffle(deck)
    #show_deck(deck)
    #show_backs()
    return deck

def games():
    game = raw_input_bens('\nWhat do you want to play?\n - Blackjack "b"\n - Texas-Holdem "t"\n')
    if game == 'blackjack' or game=='b':
        from games.blackjack import *
        deck=new_shuffled_deck()
        blackjack(deck)
    if game == 'texas-holdem'or game=='t':
        from games.texas_holdem import *
        deck=new_shuffled_deck()
        texas_holdem(deck)
    if game == 'exit':
        exit_process()

def suit_line():
    for n in range(10):
        for suit in suits:
            print suit,
    print white

def intro():
    suit_line()
    print greentable+"                      WeLcOmE 2 bEn'S cAsIn0 !                                  "+white
    suit_line()

def raw_input_bens(str):
    opt = raw_input(output_colour+str+input_colour)
    print white,
    return opt

def default_options(opt):
    if str(opt) =='exit':
        exit_process()

    if str(opt) == 'stats':
        leaderboard()
        my_name = who_am_i()
        plot_stats(my_name)
        play_again(deck)

    if str(opt) == 'help':
        from betting import betting_help
        betting_help()
        from games.blackjack import blackjack_help
        blackjack_help()

    if str(opt) == 'quit':
        games()

def clear():
    print(chr(27) + "[2J")