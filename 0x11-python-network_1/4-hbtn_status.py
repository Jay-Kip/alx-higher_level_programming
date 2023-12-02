#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests


def main():
    url = "https://alx-intranet.hbtn.io/status"

    resp = requests.get(url)

    if resp.status_code == 200:
        content = resp.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")

    else:
        print(f"An error occured: {response.status_code}")


if __name__ == "__main__":
    main()
