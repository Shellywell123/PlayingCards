from accounts import *

def dev_opts(opt):
    if opt == 'reset-debts' or opt == 'rd':
        reset_debts()
    if opt == 'delete-account' or opt == 'da':
        users,bals,debts= get_accounts()
        print users
        opt2 = raw_input_bens('which account do you want to delete?\n')
        default_options(opt2)
        if opt2 not in users:
            print opt2+' is not an account\n'
            dev_opts(opt)
        else:
            delete_account(opt2)

def opt_string_maker(thing,flag):
    optstring = output_colour+thing+' ('+input_colour+flag+output_colour+')\n'
    return optstring

def dev_menu():
    print 'Welcome to Developer Menu\n'
    ops1 = opt_string_maker('reset all account debts','rd')
    ops2 = opt_string_maker('delete an account','da')
    optstring = ops1 + ops2
    opt = raw_input_bens(optstring)
    dev_opts(opt)
