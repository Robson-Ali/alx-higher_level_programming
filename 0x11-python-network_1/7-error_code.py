#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


def main(argv):
    """
    Method that manage urllib.error.HTTPError exceptions and
    print: Error code: followed by the HTTP status code
    """
    han = argv[1]
    rob = requests.get(han)
    if rob.status_code == requests.codes.ok:
        print(rob.text)
    else:
        print("Error code: {}".format(rob.status_code))


if __name__ == "__main__":
    main(argv)
