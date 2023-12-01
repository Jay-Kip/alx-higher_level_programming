#!/usr/bin/python3
'''Post request'''
import sys
import urllib.request
import urllib.parse


def main():
    '''Sends a post request rith param=email'''
    url = sys.argv[1]
    email = sys.argv[2]

    param = {'email': email}
    data = urllib.parse.urlencode(param)
    data = data.encode('UTF8')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(url) as resp:
        feedback = resp.read()
        print(feedback.decode('UTF8'))

if __name__ == "__main__":
    main()
