#!/usr/bin/python3
'''Handles HTTP Errors using'''
import sys
import requests


def main():
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

    else:
        print(response.text)


if __name__ == "__main__":
    main()
