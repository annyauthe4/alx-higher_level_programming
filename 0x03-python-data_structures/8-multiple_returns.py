#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        length, first_char = len(sentence), sentence[0]
        return length, first_char
