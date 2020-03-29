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

def blackjack(deck):
    print '\n'*5
    print'-'*100
    global count
    deck,hand = draw(2,deck)
    count = counting(hand)

    
    def ask(deck,hand):
        show_hand(hand)
        val = evaluate_num_hand(hand)

        if val==21:
            print green,val, '!',white
            blackjack(deck)

        if val>21:
            print red,val, 'bust!',white
            blackjack(deck)

        else:

            opt=raw_input("{} hit or stand?\n".format(val))

            if str(opt) == 'hit':
                deck,hit = draw(1,deck)
                newcount = counting(hit)
                count = newcount
                hand = hand + hit
                ask(deck,hand)

            if str(opt) == 'stand':
                blackjack(deck)
                #opt2 = raw_input('play again?\n')
                #if opt2 == 'yes':
                #    blackjack(deck)
                #else:
                #    return 0

            if str(opt) == 'help':
                print green,'''\n\n\nOptions
-------------------------------
"hit"   = another card,
"stand" = stick with current hand,
"exit"  = quit game
                ''',white
                blackjack(deck)

            if str(opt) == 'exit':
                print 'goodbye ...'
                return 0

            else:
                print red,'"',str(opt),'" is not a valid input, pls type "hit" or "stand"',white
                ask(deck,hand)

    ask(deck,hand)


