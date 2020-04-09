def exit_process():
    from accounts import who_am_i,refresh_account,leaderboard
    print 'goodbye {}...'.format(who_am_i())
    refresh_account()
    leaderboard()
    exit(0)

def games(deck):
    game = raw_input_bens('\nWhat do you want to play?\n - Blackjack "b"\n - Texas-Holdem "t"\n')
    if game == 'blackjack' or game=='b':
        from games.blackjack import *
        blackjack(deck)
    if game == 'texas-holdem'or game=='t':
        from games.texas_holdem import *
        texas_holdem(deck)

def suit_line():
    from deck import suits,white
    for n in range(10):
        for suit in suits:
            print suit,
    print white

def intro():
    from deck import greentable,white,red
    suit_line()
    print greentable+"                      WeLcOmE 2 bEn'S cAsIn0 !                                  "+white
    suit_line()

def raw_input_bens(str):
    from deck import red,white
    opt = raw_input(str+red)
    print white,
    return opt