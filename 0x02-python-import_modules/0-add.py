#!/usr/bin/python3

# Import the add function from the add_0 module
from add_0 import add


def main():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()
