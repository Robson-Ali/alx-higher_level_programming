#!/usr/bin/python3
"""
Module using request that fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    han = 'https://intranet.hbtn.io/status'
    rob = requests.get(han)
    print('Body response:')
    print('\t- type: {}'.format(type(rob.text)))
    print('\t- content: {}'.format(rob.text))

if __name__ == "__main__":
    main()
