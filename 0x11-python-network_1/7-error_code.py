#!/usr/bin/python3
'''Handles HTTP Errors using'''
import sys
import requests


def main():
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {status_code}")

    else:
        print(response)


if __name__ == "__main__":
    main()
