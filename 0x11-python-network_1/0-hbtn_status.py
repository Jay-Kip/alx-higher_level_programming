#!/usr/bin/python3
'''Fetches "https://alx-intranet.hbtn.io/status" '''
import urllib.request


def main():

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        html = resp.read()
        # print("Body response:")
        # print("Body response:")
        # print(f"\t- type: {type(html)}")
        # print(f"\t- content: {html}")
        # print(f"\t- utf8 content: {html.decode()}")
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))


if __name__ == "__main__":
    main()
