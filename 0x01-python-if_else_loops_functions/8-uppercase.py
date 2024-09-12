#!/usr/bin/python3

# uppercase - converts char to uppercase
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= c <= 'z':
            result += chr(ord(char) - 32)
        result += char
    print("{}".format(result))
