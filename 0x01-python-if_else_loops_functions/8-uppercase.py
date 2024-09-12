#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= c <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
