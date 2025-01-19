#!/usr/bin/python3
"""
Fetches a url address using urllib and printing a formatted
body response
"""
import urllib.request


def fetch_status():
    """Fetches the status code of a url"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == '__main__':
    fetch_status()
