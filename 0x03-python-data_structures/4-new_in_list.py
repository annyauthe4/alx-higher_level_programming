#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_list_len = len(my_list)
    chg_list = my_list[:]

    if idx < 0 or idx >= my_list_len:
        return chg_list
    else:
        chg_list[idx] = element
        return chg_list
