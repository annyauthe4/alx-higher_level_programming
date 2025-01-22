#!/usr/bin/python3
"""Takes in URL and an email and send a POST request to it."""

import requests
import sys


def post_email():
    """Post email to a URL."""
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print("Your email is:", response.form.get('email'))


if __name__ == '__emial__':
    post_email()
