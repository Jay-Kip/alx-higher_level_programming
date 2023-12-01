#!/usr/bin/python3
import urllib.request
import sys


def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        html = resp.read()
        print(resp.headers)

if __name__ == "__main__":
    main()
