#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:
    a = -a
if a > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, a))
elif (a < 6) and (a != 0):
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, a))
else:
    print("Last digit of {} is {} and is 0".format(number, a))
