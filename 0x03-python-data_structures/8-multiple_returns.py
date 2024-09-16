#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        length, first_char = len(sentence), sentence[0]
    else:
        length, first_char = 0, None
    return length, first_char
