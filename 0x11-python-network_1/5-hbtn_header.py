#!/usr/bin/python3
"""Get header value of a URL."""

import requests
import sys


def get_header_value():
    """Gets header value of a URL."""
    url = sys.argv[1]
    response = requests.get(url).headers.get('X-Request-Id')
    print(response)


if __name__ == '__main__':
    get_header_value()
