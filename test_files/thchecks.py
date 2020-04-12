from collections import Counter

def dups(listofthings):
    d =dict(Counter(listofthings))                                                                                       
    for thing in d:
        numofdups=d[thing]
        print thing,numofdups

a = [1,2,3,4,5,1]

dups(a)