"""
Script that fetches https://intranet.hbtn.io/status
#!/usr/bin/python3
"""

import urllib.request

if __name__ == "__main__":
    rob = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(rob) as response:
        html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf8')))