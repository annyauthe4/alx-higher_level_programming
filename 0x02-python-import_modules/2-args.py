#!/usr/bin/python3


import argparse


def main():
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Add an argument that accepts a variable number of arg
    parser.add_argument("name", nargs="*")

    # Parse the arguments
    args = parser.parse_args()

    names = args.name
    arg_count = len(names)
    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:\n{}: {}"
              .format(arg_count, arg_count, names[0]))
    elif arg_count > 1:
        print("{} arguments:".format(arg_count))
        for i in range(1, arg_count + 1):
            print("{}: {}".format(i, names[i - 1]))


if __name__ == "__main__":
    main()
