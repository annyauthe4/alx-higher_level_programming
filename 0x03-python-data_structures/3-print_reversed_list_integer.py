#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list_idx = len(my_list) - 1
    while my_list_idx > -1:
        print("{:d}".format(my_list[my_list_idx]))
        my_list_idx -= 1
