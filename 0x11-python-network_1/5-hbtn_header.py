#!/usr/bin/python3
''' sends a request to the URL and displays
the value of the variable X-Request-Id in the
response header'''
import sys
import requests


def main():
    url = sys.argv[1]

    resp = requests.get(url)

    if resp.status_code == 200:
        X_request = resp.headers.get('X-Request-Id')
        print(X_request)


if __name__ == "__main__":
    main()
