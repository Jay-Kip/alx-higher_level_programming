#!/usr/bin/python3
'''Uses github API to display my id'''
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    username = sys.argv[1]
    passwd = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(username, passwd))

    if response.status_code == 200:
        profile = response.json()
        print(profile['id'])
    else:
        print("None")


if __name__ == "__main__":
    main()
