#!/usr/bin/python3
'''t takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in
the header of the response.
'''
import urllib.request
import sys


def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        X_request = resp.headers.get('X-Request-Id')
        print(X_request)


if __name__ == "__main__":
    main()
