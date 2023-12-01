#!/usr/bin/python3
'''manage urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
'''
import sys
import urllib.request


def main():
    '''Handles HTTP Errors'''
    url = sys.argv[1]

    with urllib.request.urlopen(url) as resp:
        try:
            html =resp.read()
            print(html)

        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} {e.reason}")
            # Handle the HTTP error as needed

if __name__ == "__main__"
main()
