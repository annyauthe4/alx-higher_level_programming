#!/usr/bin/python3

# print_last_digit - Prints last digit of a number
def print_last_digit(number):
    r = abs(number) % 10
    print("{:d}".format(r))
    return r
