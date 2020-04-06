from deck import *
from betting import *
from console import *
from accounts import *

#printer = [[0,0]]
#winlose = [[0,0]]
count = 0

def evaluate_num(num):
    if num == 'A':
        return 11

    if num in ['J','Q','K']:
        return 10

    if num in ['2','3','4','5','6','7','8','9','10']:
        return int(num)

def counting(hand):
    global count
    plusone = ['2','3','4','5','6']
    meh = ['7','8','9']
    negone = ['10','J','Q','K','A']

    for card in hand:
        num,suit = getinfo(card)
        if num in plusone:
            count = count + 1
            print num,'= +1'

        if num in negone:
            count = count - 1
            print num,'= -1'

        if num in meh:
            count = count
            print num,'= +0'
    
    print 'Total Count = ',count    
    save_count(count)
    return count

def evaluate_num_hand(hand):
    hand_val = 0

    for card in hand:
        num,suit = getinfo(card)
       # print num
        cardval = evaluate_num(num)
        hand_val = hand_val + cardval
        #print evaluate_num(num)

    nums=[]
    for card in hand:
        num,suit=getinfo(card)
        nums.append(num)

    
    for i in nums:
        if i is 'A':
            if hand_val > 21:
                hand_val -= 10

    return hand_val

def exit_process():
    print 'goodbye {}...'.format(who_am_i())
    refresh_account()
    leaderboard()
    exit(0)

def play_again(deck):

    width,hight = terminal_size()
    print'-'*width

    bc = broke_check()

    if bc == True:
        print 'YOU ARE BROKE'
        set_balance(1000)
        opt2 = raw_input('start again?\n')
    else:
        opt2 = raw_input('play again?\n')

    if opt2 == 'yes' or opt2 =='y' or opt2 =='':
        blackjack(deck)
    if opt2 =='no' or opt2 =='n' or opt2 =='exit':
        exit_process()
    if opt2 == 'stats':
        leaderboard()
        my_name = who_am_i()
        plot_stats(my_name)
        play_again(deck)
    if opt2 not in ['n','no','yes','y','','exit','stats']:
        print '"'+opt2+'" is not a valid input, pls type "yes/y" or "no/n"'
        play_again(deck)
    
def clear():
    print(chr(27) + "[2J")

def show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val,blind=False):
    
    width,hight = terminal_size()
    print'-'*width
    count = counting([dealers_hand[0]]+hand)
    print'-'*width

    if blind==True:
        print '\n'+bluetable+"DEALER'S HAND =",dealers_val_blind,
        show_half_hand_bet(dealers_hand,'dealers',bg=bluetable)
    else:
        print '\n'+bluetable+"DEALER'S HAND =",dealers_val,
        show_hand_bet(dealers_hand,'dealers',bg=bluetable)

    print '\n'+greentable+"YOUR HAND =",val,
    show_hand_bet(hand,'',bg=greentable)
    print white
 #   showbets()

def blackjack(deck):

    #initalise games
    user_query()
    
    deck,dealers_hand = draw(2,deck)
    deck,hand = draw(2,deck)
    
    balance = ret_balance()
   # print 'ret bal='+str(balance)

    showbets()
    prev_bet =  ret_prev_bet()
    if prev_bet>0:
        prev_bet_str = "\nPress enter to bet $"+str(prev_bet)+" again."
    else:
        prev_bet_str = ''
    bi = raw_input("How much do you want to buy in?\n(NB every hit will cost you this amount again)"+prev_bet_str+"\n$")
    if bi == 'stats':
        leaderboard()
        my_name = who_am_i()
        plot_stats(my_name)
        blackjack(deck)
    if bi =='exit':
        exit_process()        
    if bi == '':
        bi = prev_bet
    try:
        bi = int(bi)
    except:
        print red+'"'+str(bi)+'" invalid input please use integer amount\n'+white
        blackjack(deck)
    if bi <=0:
        print red+'"'+str(bi)+'" invalid input please use postive amount\n'+white
        blackjack(deck)
    if bi>balance:
        print red+'"'+str(bi)+'"is more money than you have! ($'+str(balance)+'). Place a lower bet'+white
        blackjack(deck)
    
        
    buyin(bi)

    def ask(deck,hand,dealers_hand,headless=False):

        val = evaluate_num_hand(hand)
        dealers_val = evaluate_num_hand(dealers_hand)
        dealers_val_blind = evaluate_num_hand([dealers_hand[0]])

        if headless==True:
            pass
        else:
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val,blind=True)

        if val==21:            
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
            print green,val,'!',white
            win()
            save_winlose(1)
            play_again(deck)

        if val>21:
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
            print red+str(val)+' BUST!'+white
            lose()
            save_winlose(-1)
            play_again(deck)

        else:

            opt=raw_input("\n{}Hit, Stand or Fold?{}\n".format(yellow,white))

            if str(opt) == 'exit':
                exit_process()

            if (str(opt) == 'hit') or (str(opt) =='h'):
                
                choice = raisee(bi)
                if choice == True:
                    deck,hit = draw(1,deck)
                    newcount = counting(hit)
                    count = newcount
                    hand = hand + hit
                    ask(deck,hand,dealers_hand)
                else:
                    ask(deck,hand,dealers_hand,headless=True)
            
            if (str(opt)=='fold') or (str(opt)=='f'):
                print 'YOU FOLD'
                lose()
                save_winlose(-1)
                play_again(deck)

            if (str(opt)=='stand') or (str(opt)=='s'):

                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print 'YOU STAND'
                if dealers_val == val:
                    print "PUSH",white
                    push()
                    save_winlose(0)
                    play_again(deck)

                if dealers_val < val:
                    
                    deack,dealers_hit = draw(1,deck)
                    dealers_hand = dealers_hand + dealers_hit
                    dealers_val_new = evaluate_num_hand(dealers_hand)
                    show_table(dealers_hand,hand,dealers_val_new,dealers_val_blind,val)
                    print yellow+'DEALER HITS'+white

                    if dealers_val_new>21:
                        print red+'DEALER BUST'+white
                        print green+"YOU WIN!"+white
                        win()
                        save_winlose(1)
                        play_again(deck)

                    else:

                        if dealers_val_new < val:
                            print green+"YOU WIN!"+white
                            win()
                            save_winlose(1)
                            play_again(deck)

                        if dealers_val_new>val:
                            print red+"DEALER WINS"+white
                            lose()
                            save_winlose(-1)
                            play_again(deck)

                        if dealers_val_new == val:
                            print "PUSH"+white
                            push()
                            save_winlose(0)
                            play_again(deck)

                if dealers_val > val:
                    print red+"DEALER WINS"+white
                    lose()
                    save_winlose(-1)
                    play_again(deck)
                #else:
                #    print 'missed'

            if str(opt) == 'stats':
                leaderboard()
                my_name = who_am_i()
                plot_stats(my_name)
                play_again(deck)

            if str(opt) == 'help':
                print green,'''\nOptions
-------------------------------
"hit" or "h"   = another card,
"stand" or "s" = stick with current hand,
"exit"  = quit game
                ''',white
                ask(deck,hand,dealers_hand,headless=True)

            if str(opt) not in ['stant','s','hit','h','help','exit','fold','f']:
                print red,'"'+str(opt)+'" is not a valid input, pls type "hit/h","stand/s" o "Fold/f".\n For more options type "help".',white
                ask(deck,hand,dealers_hand,headless=True)

    ask(deck,hand,dealers_hand)

hand_num = 0

def blackjack_CPU(deck,lim):

    global hand_num
    hand_num = hand_num + 1

    if hand_num == lim:
        my_name = who_am_i()
        print 'num of hands played = '+str(lim)
        plot_stats(my_name)
        refresh_account()
        leaderboard()
        exit(0)
    else:
        #initalise games
        set_name('CPU')
        user_query()
        
        deck,dealers_hand = draw(2,deck)
        deck,hand = draw(2,deck)
        
        balance = ret_balance()
        prev_bet =  ret_prev_bet()
        bi = 10     
        buyin(bi)

        def ask(deck,hand,dealers_hand,headless=False):

            val = evaluate_num_hand(hand)
            dealers_val = evaluate_num_hand(dealers_hand)
            dealers_val_blind = evaluate_num_hand([dealers_hand[0]])

            if headless==True:
                pass
            else:
                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val,blind=True)

            if val==21:            
                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print green,val,'!',white
                win()
                save_winlose(1)
                blackjack_CPU(deck,lim)

            if val>21:
                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print red+str(val)+' BUST!'+white
                lose()
                save_winlose(-1)
                blackjack_CPU(deck,lim)

            if 7<=val<=17:
                choice = raisee(bi)
                if choice == True:
                    deck,hit = draw(1,deck)
                    newcount = counting(hit)
                    count = newcount
                    hand = hand + hit
                    ask(deck,hand,dealers_hand,headless=True)
            
            if val<=7:
                print 'YOU FOLD'
                lose()
                save_winlose(-1)
                blackjack_CPU(deck,lim)

            if val>=18:

                print 'YOU STAND'
                if dealers_val == val:
                    print "PUSH",white
                    push()
                    save_winlose(0)
                    blackjack_CPU(deck,lim)

                if dealers_val < val:
                    
                    deack,dealers_hit = draw(1,deck)
                    dealers_hand = dealers_hand + dealers_hit
                    dealers_val_new = evaluate_num_hand(dealers_hand)
                    show_table(dealers_hand,hand,dealers_val_new,dealers_val_blind,val)
                    print yellow+'DEALER HITS'+white

                    if dealers_val_new>21:
                        print red+'DEALER BUST'+white
                        print green+"YOU WIN!"+white
                        win()
                        save_winlose(1)
                        blackjack_CPU(deck,lim)

                    else:

                        if dealers_val_new < val:
                            print green+"YOU WIN!"+white
                            win()
                            save_winlose(1)
                            blackjack_CPU(deck,lim)

                        if dealers_val_new>val:
                            print red+"DEALER WINS"+white
                            lose()
                            save_winlose(-1)
                            blackjack_CPU(deck,lim)

                        if dealers_val_new == val:
                            print "PUSH"+white
                            push()
                            save_winlose(0)
                            blackjack_CPU(deck,lim)

                if dealers_val > val:
                    print red+"DEALER WINS"+white
                    lose()
                    save_winlose(-1)
                    blackjack_CPU(deck,lim)

        ask(deck,hand,dealers_hand,headless=True)
