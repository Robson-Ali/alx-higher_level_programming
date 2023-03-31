#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import requests
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    han = argv[1]
    rob = requests.post(han, data=values)
    print(rob.text)

if __name__ == "__main__":
    main(argv)
