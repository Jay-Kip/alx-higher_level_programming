#!/usr/bin/python3
'''sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.'''
import sys
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"
    arg = sys.argv[1]

    if len(arg) > 1:
        letter = arg[1]

    else:
        letter = ""

    param = {"q": letter}

    response = requests.post(url, data=param)

    try:
        json_data = response.json()
        if json_data:
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")

        except ValueError:
            print("Not a valid JSON")
