#!/usr/bin/python3
'''takes in a URL and an email address, sends a
POST request to the passed URL with the email as
a parameter, and finally displays the body of the respons
'''
import sys
import requests

def main():
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary of paramaters
    param = {'email': email}

    # Send post request with params
    response = requests.post(url, data=param)

    if response.status_code == 200:
        content = response.text
        print(content)

    else:
        print(f"An error occured: {response.status_code}")


if __name__ == "__main__":
    main()
