#!/usr/bin/python3
def add(a, b):
    a, b = abs(a), abs(b)
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return a + b
