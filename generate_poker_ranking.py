# IMPORTANT NOTE #
# 1 = best rank (royal flush)

from deck import suits
#suits =   [spades,clubs,hearts,diamonds]

entries = []

def append_entry(name,rank,hand):
    """
    will append a ranking entry to list,
    in format
    handname,handrank,handcontents
    """
    entries.append('{},{},"{}"'.format(name,str(rank),hand))

#####################################################
# Royal flushes
#####################################################

# a = 1
# a AKQJ10 x4

royal_flushes = []
for suit in suits:

    hand = ['A'+suit, 'K'+suit, 'Q'+suit, 'J'+suit, '10'+suit]
    append_entry('Royal_Flush',1,str(hand))

#####################################################
# Straight flushes
#####################################################

# b = a+1
# b   910JQK x4
# b+1 8910JQ x4
# b+2 78910J x4
# b+3 678910 x4
# b+4 56789  x4
# b+5 45678 x4
# b+6 34567 x4
# b+7 23456 x4
# b+8 A2345 x4

#####################################################
# Four of a Kind
#####################################################

# c =b+1

# c   AAAAK x4
# c+1 AAAAQ x4
# c+2 AAAAJ x4
# etc

#####################################################
# Full house (three of a kind + pair)
#####################################################

# d = c+1
# d   AAAKK x?
# d+1 does KKKAA beat AAAQQ

#####################################################
# Flush
#####################################################

# e = d+1
# e   9JQKA x ?
# 

#####################################################
# Straight
#####################################################

# f = e+1

# f   910JQK x?
# f+1 8910JQ x?
# f+2 78910J x?
# f+3 678910 x?
# f+4 56789  x?
# f+5 45678 x?
# f+6 34567 x?
# f+7 23456 x?
# f+8 A2345 x?


#####################################################
# Three of a Kind
#####################################################

# g = f+1
# g   AAAKQ x?
# g+1 AAAQJ

#####################################################
# Two pair
#####################################################

# h = g+1
# h   AAKKQ x?
# h+1 AAKKJ x?

#####################################################
# One pair
#####################################################

# i = h+1
# h   AAKQJ x?


#####################################################
# High Card
#####################################################

# j = i+1
# j AKQJ9 x?


# write entries out to csv
f = open("data/poker_hand_rankings.csv", "a")
for entry in entries:
    f.write(str(entry)+'\n')
f.close()
