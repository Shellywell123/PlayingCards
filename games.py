from deck import *

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
            print 'count = ',count

        if num in negone:
            count = count - 1
            print 'count = ',count

        if num in meh:
            count = count
            print 'count = ',count

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
    opt2 = raw_input('play again?\n')
    if opt2 == 'yes' or opt2 =='':
        blackjack(deck)
    else:
        exit(0)

def blackjack(deck):
    print '\n'*5
    print'-'*100
    global count

    deck,dealers_hand = draw(2,deck)
    deck,hand = draw(2,deck)
    count = counting(hand)

    
    def ask(deck,hand,dealers_hand):

        val = evaluate_num_hand(hand)
        dealers_val = evaluate_num_hand(dealers_hand)

        print '\n'+white+"DEALER'S HAND =",dealers_val,
        show_hand(dealers_hand)

        print '\n'+greentable+"YOUR HAND =",val
        show_hand(hand,bg=greentable)
        print white

        if val==21:
            print green,val, '!',white
            play_again(deck)

        if val>21:
            print red,val, 'bust!',white
            play_again(deck)

        else:

            opt=raw_input("\n{}hit or stand?{}\n".format(yellow,white))

            if str(opt) == 'exit':
                print 'goodbye ...'
                exit(0)

            if str(opt) == 'hit'or str(opt) =='h':
                deck,hit = draw(1,deck)
                newcount = counting(hit)
                count = newcount
                hand = hand + hit
                ask(deck,hand,dealers_hand)

            if str(opt) == 'stand'or str(opt) =='s':
                if dealers_val == val:
                    print "draw",white
                    play_again(deck)

                if dealers_hand > val:
                    print green,"you win!",white
                    play_again(deck)

                if dealers_val < val:
                    print red,"dealer wins",white
                    play_again(deck)

            if str(opt) == 'help':
                print green,'''\n\n\nOptions
-------------------------------
"hit" or "h"   = another card,
"stand" or "s" = stick with current hand,
"exit"  = quit game
                ''',white
                blackjack(deck)

            else:
                print red,'"',str(opt),'" is not a valid input, pls type "hit" or "stand"',white
                ask(deck,hand,dealers_hand)

    ask(deck,hand,dealers_hand)


