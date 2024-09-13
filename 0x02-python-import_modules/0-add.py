#!/usr/bin/python3

# Import the add function from the add_0 module
from add_0 import add


def main():
    a = 1
    b = 2
    result = add(1, 2)
    print("{} + {} = {}".format(a, b, result))


if __name__ == "__main__":
    main()
