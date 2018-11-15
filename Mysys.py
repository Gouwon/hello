import os

def mysis():
    if os.name == 'nt':
        os.system('CLS')
    else:  # posix
        os.system('clear')

mysis()

