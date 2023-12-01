#!/usr/bin/python3
'''Fetches "https://alx-intranet.hbtn.io/status" '''
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    html = resp.read()
    print("Body response :")
    print(f"\t-\ttype : {type(html)}")
    print(f"\t-\tcontent : {html}")
    print(f"\t-\tutf8 content : {html.decode()}")
