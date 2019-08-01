#!/usr/bin/python3

import requests
from colorama import Fore, Back, Style

file = './page'
pageSuccess = list()
target = input('URL >')
with open(file, 'r') as pages:
    for page in pages.readlines():
        try:
            url = target + page.replace("\n","")
            res = requests.get(url)
            if res.status_code == 200:
                print(Fore.GREEN + '[OK] ' + url)
                pageSuccess.append(url)
            else:
                print(Fore.RED + '[FAIL] ' + url)
        except KeyboardInterrupt:
            print('\n')
            break

for success in pageSuccess:
    print(Fore.GREEN + success)
print(Style.RESET_ALL)
