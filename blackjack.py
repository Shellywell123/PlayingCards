from deck import *
from betting import *
from console import *



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

    #import matplotlib.pyplot as plt
    #plt.xlabel('num of cards')
    #plt.ylabel('count')
    #plt.plot(len(hand),count)
    #plt.grid()
    #plt.show()
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

def play_again(deck):
    width,hight = terminal_size()
    print'-'*width

    opt2 = raw_input('play again?\n')

    if opt2 == 'yes' or opt2 =='y' or opt2 =='':
        blackjack(deck)
    if opt2 =='no' or opt2 =='n' or opt2 =='exit':
        exit(0)
    if opt2 not in ['n','no','yes','y','','exit']:
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
        show_half_hand(dealers_hand,bg=bluetable)
    else:
        print '\n'+bluetable+"DEALER'S HAND =",dealers_val,
        show_hand(dealers_hand,bg=bluetable)

    print '\n'+greentable+"YOUR HAND =",val,
    show_hand(hand,bg=greentable)
    print white

def blackjack(deck):

    #initalise games
    
    deck,dealers_hand = draw(2,deck)
    deck,hand = draw(2,deck)
    
    showbets()

    bi = int(raw_input("How much do you want to buy in?\n(NB every hit will cost you this amount again)\n$"))
    if bi <0:
        print '"'+str(bi)+'" invalid input please use postive amount\n'
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
            play_again(deck)

        if val>21:
            show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
            print red+str(val)+' BUST!'+white
            lose()
            play_again(deck)

        else:

            opt=raw_input("\n{}Hit or Stand?{}\n".format(yellow,white))

            if str(opt) == 'exit':
                print 'goodbye ...'
                exit(0)

            if (str(opt) == 'hit') or (str(opt) =='h'):
                deck,hit = draw(1,deck)
                newcount = counting(hit)
                count = newcount
                hand = hand + hit
                raisee(bi)
                ask(deck,hand,dealers_hand)

            if (str(opt)=='stand') or (str(opt)=='s'):

                show_table(dealers_hand,hand,dealers_val,dealers_val_blind,val)
                print 'YOU STAND'
                if dealers_val == val:
                    print "PUSH",white
                    push()
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
                        play_again(deck)

                    else:

                        if dealers_val_new < val:
                            print green+"YOU WIN!"+white
                            win()
                            play_again(deck)

                        if dealers_val_new>val:
                            print red+"DEALER WINS"+white
                            lose()
                            play_again(deck)

                        if dealers_val_new == val:
                            print "PUSH"+white
                            push()
                            play_again(deck)

                if dealers_val > val:
                    print red+"DEALER WINS"+white
                    lose()
                    play_again(deck)
                #else:
                #    print 'missed'

            if str(opt) == 'help':
                print green,'''\nOptions
-------------------------------
"hit" or "h"   = another card,
"stand" or "s" = stick with current hand,
"exit"  = quit game
                ''',white
                ask(deck,hand,dealers_hand,headless=True)

            if str(opt) not in ['stant','s','hit','h','help','exit']:
                print red,'"'+str(opt)+'" is not a valid input, pls type "hit/h" or "stand/s".\n For more options type "help".',white
                ask(deck,hand,dealers_hand,headless=True)

    ask(deck,hand,dealers_hand)


