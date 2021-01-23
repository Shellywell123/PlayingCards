cdfrom betting import *
from general.general import *

name = ''
accounts_path = "data/accounts.txt"

def get_accounts():
    text_file = open(accounts_path, "r")
    lines = text_file.readlines()
    
    users = []
    balances = []
    debts = []

    for line in lines:
        user = line.split(':')[0]
        balance = line.split(':')[1]
        debt = line.split(':')[2]
        if balance[-1:] =='\n':
            balance = balance[:-1]
        users.append(user)
        balances.append(balance)
        debts.append(debt)

    if len(users)==0:
        return [],[]

    return users,balances,debts

def set_name(name_):
    global name
    name = name_

def user_query():
    global name 
    if name == 'dev':
        #needs to be cleared when exiting dev menu
        name = ''
    
    users,user_balances,debts = get_accounts()

    if name in users:
        user = name
        print ('Welcome back '+name+'!')
        user_balance = user_balances[users.index(user)]
        set_balance(int(user_balance))

    if name not in users:

        if name == '':
            name = raw_input_bens("Who are you?\n")

        if name == 'dev':
            from general.dev import dev_menu
            dev_menu()
            user_query()

        if name == 'exit':
            print ('Goodbye ...')
            exit(0)
        if name in users:
            user = name
            print ('Welcome back '+name+'!')
            user_balance = user_balances[users.index(user)]
            set_balance(int(user_balance))
        else:
            print ('Welcome '+name+'!')
            make_account(name)

def make_account(name):
    users,bals,debts= get_accounts()
    text_file = open(accounts_path, "a")
    text_file.write(name+':'+str(1000)+':'+str(0)+':'+'\n')
    text_file.close()

def delete_account(user):
    users,balances,debts = get_accounts()

    text_file = open(accounts_path, "w")
    for n in range(len(users)):
        if users[n] == user:
            pass
        else:
            text_file.write(users[n]+':'+balances[n]+':'+debts[n]+':'+'\n')
    text_file.close()

    users,balances,debts = get_accounts()
    print (users)
    print (user+"'s account has been deleted")

def reset_debts():
    name = who_am_i()
    users,balances,debts = get_accounts()

    text_file = open(accounts_path, "w")
    for n in range(len(users)):
        text_file.write(users[n]+':'+balances[n]+':'+str(0)+':'+'\n')
        print (debts[n],)
    text_file.close()

def refresh_account(debt_added=0):
    name = who_am_i()
    users,balances,debts = get_accounts()

    old_balance = balances[users.index(name)]
    old_debt = debts[users.index(name)]

    debt = int(old_debt) + debt_added

    if debt >0:
        print ('your account has now loaned $'+str(debt))
    new_balance = ret_balance()

    balances[users.index(name)] = str(new_balance)
    debts[users.index(name)] = str(debt)

    text_file = open(accounts_path, "w")
    for n in range(len(users)):
        text_file.write(users[n]+':'+balances[n]+':'+str(debts[n])+':'+'\n')
    text_file.close()

def read_accounts():
    text_file = open(accounts_path, "r")
    lines = text_file.readlines()
    text_file.close()

def who_am_i():
    global name
    return name

def leaderboard():
    users,balances,debts = get_accounts()

    for n in range(len(balances)):
        balances[n] = int(balances[n])

    balances,users = zip(*sorted(zip(balances, users)))        
    balances = list(reversed(balances))
    users = list(reversed(users))

    print ('\n'+'-'*15)
    print ('LEADERBOARD')
    for i in range(len(users)):
        print (str(i+1)+') '+users[i]+' $'+str(balances[i]))
 