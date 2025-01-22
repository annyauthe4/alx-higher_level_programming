#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code.
"""
import urllib.request
import urllib.error
import sys


def print_error_code():
    """Fetch and print URL body or error code."""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
        print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == '__main__':
    print_error_code()
