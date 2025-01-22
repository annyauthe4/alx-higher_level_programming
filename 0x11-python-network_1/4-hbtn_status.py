#!/usr/bin/python3
"""Prints status code of a URL using requests."""

import requests


def fetch_status_res():
    """Fetches URL and print status code."""
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))


if __name__ == '__main__':
    fetch_status_res()
