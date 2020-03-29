from deck import *

def evaluate_num(num):
    if num == 'A':
        return 11

    if num in ['J','Q','K']:
        return 10

    if num in ['2','3','4','5','6','7','8','9','10']:
        return int(num)

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
    print'-'*100
    global count
    deck,hand = draw(2,deck)
    count = counting(hand)

    
    def ask(deck,hand):
        show_hand(hand)
        val = evaluate_num_hand(hand)

        if val>21:
            print val, 'bust!'

        else:

            opt=raw_input("{} hit or stand?\n".format(val))

            if str(opt) == 'hit':
                deck,hit = draw(1,deck)
                newcount = counting(hit)
                count = newcount
                hand = hand + hit
                ask(deck,hand)

            if str(opt) == 'stand':
                opt = raw_input('play again?\n')
                if opt == 'yes':
                    blackjack(deck)

    ask(deck,hand)


