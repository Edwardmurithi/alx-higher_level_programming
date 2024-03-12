#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cast_str = str(number)
x = cast_str[-1]
cast_int = int(x)
if cast_int > 5:
    print(f"Last digit of {number:d} is {x:s} and is greater than 5")
elif cast_int == 0:
    print(f"Last digit of {number:d} is {x:s} and is 0")
else:
    print(f"Last digit of {number:d} is {x:s} and is less than 6 and not 0")
