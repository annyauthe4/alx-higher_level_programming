#!/usr/bin/python3

# This program imports a function from a module
from add_0 import add

def main():
    a = 1
    b = 2
    result = add(1, 2)
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()
