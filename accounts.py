from betting import *
from blackjack import *

name = ''
accounts_path = "data/accounts.txt"

def get_accounts():
    text_file = open(accounts_path, "r")
    lines = text_file.readlines()
    
    users = []
    balances = []
    for line in lines:
        user = line.split(':')[0]
        balance = line.split(':')[1]
        if balance[-1:] =='\n':
            balance = balance[:-1]
        users.append(user)
        balances.append(balance)

    if len(users)==0:
        return [],[]

    return users,balances

def set_name(name_):
    global name
    name = name_

def user_query():
    global name 
    users,user_balances = get_accounts()
    if name == '':
        name = raw_input("Who are you?\n")
    else:
        if name in users:
            user = name
            print 'Welcome back '+name+'!'
            user_balance = user_balances[users.index(user)]
            set_balance(int(user_balance))
        else:
            print 'Welcome '+name+'!'
            make_account(name)
    if name == 'exit':
        print 'Goodbye ...'
        exit(0)
    else:
        pass

def make_account(name):
    users,bals= get_accounts()
    text_file = open(accounts_path, "a")
    text_file.write(name+':'+str(1000)+'\n')
    text_file.close()

def refresh_account():

    name = who_am_i()
    users,balances = get_accounts()

    old_balance = balances[users.index(name)]
    new_balance = ret_balance()
    balances[users.index(name)] = str(new_balance)

    text_file = open(accounts_path, "w")
    for n in range(len(users)):
        text_file.write(users[n]+':'+balances[n]+'\n')
    text_file.close()

def read_accounts():
    text_file = open(accounts_path, "r")
    lines = text_file.readlines()
    text_file.close()

def who_am_i():
    global name
    return name

def leaderboard():
    users,balances = get_accounts()

    for n in range(len(balances)):
        balances[n] = int(balances[n])

    balances,users = zip(*sorted(zip(balances, users)))        
    balances = list(reversed(balances))
    users = list(reversed(users))

    print '\n'+'-'*15
    print 'LEADERBOARD'
    for i in range(len(users)):
        print str(i+1)+') '+users[i]+' $'+str(balances[i])
 