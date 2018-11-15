import sys
import Mysys

# from Mysys import mysis
# mysis()

Mysys.mysis()

l = [sys.version, sys.copyright, sys.platform]

def print_sys():
    for i in l:
        print("------>{}".format(l[i]), i)

sa = sys.argv
if len(sa) < 2:
    print_sys()
    sys.exit()

with open(sa[1], "r", encoding="utf8") as file:
    for line in file:
        print(line)