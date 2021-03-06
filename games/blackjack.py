from deck import *
from betting import *
from accounts import *
from general.console import *
from general.general import *
from general.colours import *

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
            print (num,'= +1')

        if num in negone:
            count = count - 1
            print (num,'= -1')

        if num in meh:
            count = count
            print (num,'= +0')
    
    print ('Total Count = ',count    )
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
    split_check(hand)
    return hand_val

def split_check(hand):
    nums=[]
    for card in hand:
        num,suit=getinfo(card)
        nums.append(num)

    if (len(hand) == 2) and (nums[0] == nums[1]):
        return True
        #  return True
    else:
        return False

def blackjack_help():
    print (green+''' Blackjack
 -------------------------
 - "hit/h"   = another card
 - "doubledown/d" = hit + re bet last amount 
    (can only double down on 2 card hand to a 3 card hand & will end you turn.)
 - "stand/s" = stick with current hand
 - "stats" = player statistics
 - on "play again?"" prompt
   - "y" or enter = play again
   - "n" = end game
                '''+white)

def play_again(deck):

    width,hight = terminal_size()
    print('-'*width)

    bc = broke_check()

    if bc == True:
        print ('YOU ARE BROKE')
        set_balance(1000)
        refresh_account(debt_added=1000)
        opt2 = raw_input_bens('start again?\n')
    else:
        opt2 = raw_input_bens('play again?\n')

    if opt2 == 'yes' or opt2 =='y' or opt2 =='':
        blackjack(deck)
    if opt2 =='no' or opt2 =='n':
        exit_process()
    default_options(opt2)
    if opt2 not in ['n','no','yes','y','','exit','stats','help']:
        print ('"'+opt2+'" is not a valid input, pls type "yes/y" or "no/n"')
        play_again(deck)

def show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val,blind=False):
    
    width,hight = terminal_size()
    print('-'*width)
    count = counting([dealers_hand[0]]+hand)
    print('-'*width)

    if blind==True:
        print ('\n'+bluetable+"DEALER'S HAND =",dealers_val_blind,)
        show_half_hand_bet(dealers_hand,'dealers',bg=bluetable)
    else:
        print ('\n'+bluetable+"DEALER'S HAND =",dealers_val,)
        show_hand_bet(dealers_hand,'dealers',bg=bluetable)

    print ('\n'+greentable+"YOUR HAND =",val,)
    show_hand_bet(hand,'',bg=greentable)
    print (white)
 #   showbets()

def show_table_split(dealers_hand,hand1,hand2,dealers_val,val1,val2):
    width,hight = terminal_size()
    print('-'*width)
    count = counting([dealers_hand[0]]+hand1+hand2)
    print('-'*width)

    print ('\n'+bluetable+"DEALER'S HAND =",dealers_val,)
    show_hand_bet(dealers_hand,'dealers',bg=bluetable)

    print ('\n'+greentable+"YOUR HANDS =",val1,',',val2)
    show_split_hand_bet(hand1,hand2,bg1=greentable,bg2=greentable)
    print (white)

def dealer_opts(dealers_hand,hand,deck):
                    
    deck,dealers_hit = draw(1,deck)
    dealers_hand = dealers_hand + dealers_hit
    dealers_val_new = evaluate_num_hand(dealers_hand)
    val = evaluate_num_hand(hand)
    show_table(dealers_hand,hand,dealers_val_new,dealers_val_new,val)
    print (yellow+'DEALER HITS'+white)

    if dealers_val_new>21:
        print (red+'DEALER BUST'+white)
        print (green+"YOU WIN!"+white)
        win()
        save_winlose(1)
        play_again(deck)

    else:

        if dealers_val_new < val:
            if dealers_val_new <= 15:
                dealer_opts(dealers_hand,hand,deck)
            else:
                print (green+"YOU WIN!"+white)
                win()
                save_winlose(1)
                play_again(deck)

        if dealers_val_new>val:
            print (red+"DEALER WINS"+white)
            lose()
            save_winlose(-1)
            play_again(deck)

        if dealers_val_new == val:
            print ("PUSH, pot is carried to next turn"+white)
            push()
            save_winlose(0)
            play_again(deck)

def stats_opt(opt,deck):
    if str(opt) == 'stats':
        leaderboard()
        my_name = who_am_i()
        plot_stats(my_name)
        play_again(deck)

def blackjack(deck):
    #initalise games
   
    deck,dealers_hand = draw(2,deck)
    deck,hand = draw(2,deck)
    
    balance = ret_balance()
   # print 'ret bal='+str(balance)

    showbets()
    bo=betting_opts()
    if bo==False:
        blackjack(deck)
    else:
        bi=bo

    buyin(bi)


    def ask(deck,hand,dealers_hand,headless=False):

        val = evaluate_num_hand(hand)
        dealers_val = evaluate_num_hand(dealers_hand)
        dealers_val_blind = evaluate_num_hand([dealers_hand[0]])
        save_vals(val,dealers_val)

        if split_check(hand) == True:
            split_opt=output_colour+' Split('+input_colour+'sp'+output_colour+'),'
        else:
            split_opt = ''

        if headless==True:
            pass
        else:
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val,blind=True)

        if val==21:            
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
            if dealers_val==val:
                push()
                save_winlose(0)
                play_again(deck)
            else:
                print (green,val,'!',white)
                win()
                save_winlose(1)
                play_again(deck)

        if val>21:
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
            print (red+str(val)+' BUST!'+white)
            lose()
            save_winlose(-1)
            play_again(deck)

        else:
            opt=raw_input_bens("Hit("+input_colour+"h"+output_colour+"),"+split_opt+" Stand("+input_colour+"s"+output_colour+"), Double-Down("+input_colour+"d"+output_colour+") or Fold("+input_colour+"f"+output_colour+")?\n")

            default_options(opt)
            stats_opt(opt,deck)

            if (str(opt) == 'hit') or (str(opt) =='h'):
                deck,hit = draw(1,deck)
                newcount = counting(hit)
                count = newcount
                hand = hand + hit
                ask(deck,hand,dealers_hand)

            if (str(opt)=='split') or (str(opt)=='sp'):
                sc = split_check(hand)
                if sc == True:
                    hand1,hand2=split_hand(hand)
                    val1 = evaluate_num_hand(hand1)
                    val2 = evaluate_num_hand(hand2)
                    show_table_split(dealers_hand,hand1,hand2,dealers_val,val1,val2)
                    hand = hand1
                    ask(deck,hand,dealers_hand)
                else:
                    print ('you cannot split this hand!')
                    ask(deck,hand,dealers_hand)

               # betting on hit
               #
               # choice = raisee(bi)
               # if choice == True:
               #     deck,hit = draw(1,deck)
               #     newcount = counting(hit)
               #     count = newcount
               #     hand = hand + hit
               #     ask(deck,hand,dealers_hand)
               # else:
               #     ask(deck,hand,dealers_hand,headless=True)

            if (str(opt)=='doubledown') or (str(opt)=='d'):
                
                choice = raisee(bi)

                if choice == True:
                    deck,hit = draw(1,deck)
                    newcount = counting(hit)
                    count = newcount
                    hand = hand + hit
                    val = evaluate_num_hand(hand)
                    show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                    print ('DOUBLE DOWN')
                    if val >=22:
                        print (red+"BUST|\nDEALER WINS"+white)
                        lose()
                        save_winlose(-1)
                        play_again(deck)

                    if dealers_val == val:
                        print ("PUSH, pot is carried to next turn"+white)
                        push()
                        save_winlose(0)
                        play_again(deck)

                    if dealers_val < val:
                        dealer_opts(dealers_hand,hand,deck)

                    if dealers_val > val:
                        print (red+"DEALER WINS"+white)
                        lose()
                        save_winlose(-1)
                        play_again(deck)
                
            if (str(opt)=='fold') or (str(opt)=='f'):
                print ('YOU FOLD')
                lose()
                save_winlose(-1)
                play_again(deck)

            if (str(opt)=='stand') or (str(opt)=='s') or (str(opt)==''):

                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print ('YOU STAND')
                if dealers_val == val:
                    print ("PUSH, pot is carried to next turn"+white)
                    push()
                    save_winlose(0)
                    play_again(deck)

                if dealers_val < val:
                    dealer_opts(dealers_hand,hand,deck)

                if dealers_val > val:
                    print (red+"DEALER WINS"+white)
                    lose()
                    save_winlose(-1)
                    play_again(deck)
                #else:
                #    print 'missed'
            if str(opt) == 'help':
                print (green,'''\nOptions
-------------------------------
"hit" or "h"   = another card,
"stand" or "s" = stick with current hand,
"exit"  = quit game
                ''',white)
                ask(deck,hand,dealers_hand,headless=True)

            flags = [
            'stand','s',
            'split','sp'
            'soubledown','d',
            'hit','h',
            'fold','f',
            'help',
            'stats',
            'exit'
            ]   

            if str(opt) not in flags:
                print (red+'"'+input_colour+str(opt)+red+'" is not a valid input, pls type "hit/h","stand/s" o "Fold/f".\n For more options type "help".',white)
                ask(deck,hand,dealers_hand,headless=True)

    ask(deck,hand,dealers_hand)

hand_num = 0

def blackjack_CPU(deck,lim,option='til-bust'):

    global hand_num
    global count
    global count_stat
    global cardsdrawn_stat
    hand_num = hand_num + 1

    #print hand_num % 52
    if int(cardsdrawn_stat) % 52 == 0:
        deck = new_shuffled_deck()
        count = 0

    if option == 'til-bust':
        balance = ret_balance()
        if balance == 0:
            #need to reset balance as this creates a loop of 0
            set_balance(1000)
            my_name = who_am_i()
            print ('num of hands played = '+str(lim))
            plot_stats(my_name)
            refresh_account()
            leaderboard()
            exit(0) 

    if (hand_num == lim):
        my_name = who_am_i()
        print ('num of hands played = '+str(lim))
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


        if count_stat[-1][1] > 0:
            bi = balance*count_stat[-1][1]/10
        else:
            bi = 10     

        buyin(bi)

        def ask(deck,hand,dealers_hand,headless=False):

            val = evaluate_num_hand(hand)
            dealers_val = evaluate_num_hand(dealers_hand)
            dealers_val_blind = evaluate_num_hand([dealers_hand[0]])
            save_vals(val,dealers_val)

            if headless==True:
                pass
            else:
                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val,blind=True)

            if val==21:            
                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print (green,val,'!',white)
                win()
                save_winlose(1)
                blackjack_CPU(deck,lim)

            if val>21:
                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print (red+str(val)+' BUST!'+white)
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
                print ('YOU FOLD')
                lose()
                save_winlose(-1)
                blackjack_CPU(deck,lim)

            if val>=18:

                print( 'YOU STAND')
                if dealers_val == val:
                    print( "PUSH",white)
                    push()
                    save_winlose(0)
                    blackjack_CPU(deck,lim)

                if dealers_val < val:
                    
                    deack,dealers_hit = draw(1,deck)
                    dealers_hand = dealers_hand + dealers_hit
                    dealers_val_new = evaluate_num_hand(dealers_hand)
                    show_table(dealers_hand,hand,dealers_val_new,dealers_val_blind,val)
                    print (yellow+'DEALER HITS'+white)

                    if dealers_val_new>21:
                        print (red+'DEALER BUST'+white)
                        print (green+"YOU WIN!"+white)
                        win()
                        save_winlose(1)
                        blackjack_CPU(deck,lim)

                    else:

                        if dealers_val_new < val:
                            print (green+"YOU WIN!"+white)
                            win()
                            save_winlose(1)
                            blackjack_CPU(deck,lim)

                        if dealers_val_new>val:
                            print (red+"DEALER WINS"+white)
                            lose()
                            save_winlose(-1)
                            blackjack_CPU(deck,lim)

                        if dealers_val_new == val:
                            print ("PUSH"+white)
                            push()
                            save_winlose(0)
                            blackjack_CPU(deck,lim) 

                if dealers_val > val:
                    print (red+"DEALER WINS"+white)
                    lose()
                    save_winlose(-1)
                    blackjack_CPU(deck,lim)

        ask(deck,hand,dealers_hand,headless=True)

