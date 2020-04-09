from colorama import init
init()

import os
try:
    os.system('chcp 65001')
except:
    print('this can be ignored if running on  \n')
    pass

red = '\033[91m'
redcard ='\033[6;31;47m'
yellow ='\033[93m'
blue = '\033[94m'
blackcard = '\033[6;30;47m'
white='\033[0m'
green='\033[32m'
greentable =  '\033[40;42m'
bluetable = '\033[0;44m'
card_back = '\033[0;41m'
input_colour = red
output_colour = yellow