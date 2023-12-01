#!/usr/bin/python3
'''manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
'''
import sys
import urllib.request


def main():
    '''Handles HTTP Errors'''
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as resp:
            html =resp.read()
            print(html.decode('UTF8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        # Handle the HTTP error as needed

if __name__ == "__main__":
    main()
