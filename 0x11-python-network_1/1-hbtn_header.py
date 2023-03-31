#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
from sys import argv

rob = argv
with urllib.request.urlopen(rob) as response:
    hanan = response.info()
    print(hanan['X-Request-Id'])

if __name__ == "__main__":
    main(argv[1])
