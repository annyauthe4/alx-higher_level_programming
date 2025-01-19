#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the `X-Request-Id` variable found in the header of the response.
"""
import urllib.request
import sys


def fetch_header_value():
    """Fetch the id value of the URL response"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == '__main__':
    fetch_header_value()
