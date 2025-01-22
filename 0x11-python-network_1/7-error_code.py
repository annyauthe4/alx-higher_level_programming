#!/usr/bin/python3
"""Prints URL response body or error code."""

import requests
import sys


def print_error_code():
    """Prints body of response or error code."""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == '__main__':
    print_error_code()
