#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    x = abs(number) % 10
    print("Last digit of {} is {} and is ".format(number, x), end="")
    if x > 5:
        print("greater than 5")
    elif x == 0:
        print("0")
    else:
        print("less than 6 and not 0")
else:
    x = abs(number) % 10
    x = -x
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")
