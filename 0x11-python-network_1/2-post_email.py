#!/usr/bin/python3
'''sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
'''
import sys
import urllib.request
import urllib.parse


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data to be sent in the post request
    data = urllib.parse.urlencode({email: email}).encode()

    # Send the posy request
    req = urllib.request.Request(url, data=data, method='PUT')

    with urllib.request.urlopen(url) as resp:
        # Process the response
        response_data = response.read().decode()

        # print response data
        print(response_data)

if __name__ == "__main__":
    main()
