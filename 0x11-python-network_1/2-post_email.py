#!/usr/bin/python3
'''Post request'''
import sys
import urllib.request
import urllib.parse


def main():
    '''Sends a post request rith param=email'''
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary to store the parameter
    param = {'email': email}

    # Encode the parameter into a URL-encoded string
    data = urllib.parse.urlencode(param)
    data = data.encode('UTF8')

    # create a request with the URL and data
    req = urllib.request.Request(url, data)

    # Send the POST request and obtain the response
    with urllib.request.urlopen(req) as resp:
        feedback = resp.read()
        print(feedback.decode('UTF8'))

if __name__ == "__main__":
    main()
