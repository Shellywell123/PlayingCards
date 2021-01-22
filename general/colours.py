from colorama import init
init()

import os

if os.name == 'nt':
    try:
        os.system('chcp 65001')
    except:
        print('this can be ignored if running on  \n')
        pass

red        = '\033[1;91m'
yellow     = '\033[1;93m'
blue       = '\033[1;94m'
white      = '\033[1;0m'
green      = '\033[1;32m'
greentable = '\033[40;42m'
bluetable  = '\033[0;44m'
card_back  = '\033[0;41m'
pink       = '\033[1;35m'
cyan       = '\033[1;36m'

redcard    = '\033[1;31;47m'
blackcard  = '\033[0;30;47m'

input_colour  = pink
output_colour = cyan
