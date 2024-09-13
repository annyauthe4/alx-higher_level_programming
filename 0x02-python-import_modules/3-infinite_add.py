#!/usr/bin/python3


import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("number", nargs="*")
    args = parser.parse_args()

    numbers = args.number
    arg_count = len(numbers)

    if arg_count == 0:
        print("{}".format(arg_count))
    elif arg_count >= 1:
        total = 0
        for i in range(arg_count):
            total += int(numbers[i])
        print("{}".format(total))


if __name__ == "__main__":
    main()
