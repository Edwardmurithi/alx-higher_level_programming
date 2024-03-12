#!/usr/bin/python3
# Edward murithi
# <murithiedward330@gmail.com>

"""Print all the letters except q and e and not followed by new line"""
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
