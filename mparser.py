import requests
from bs4 import BeautifulSoup
import lxml
import json
import re
import time as t

mlasttime = ""
with open("result.txt", "a") as f:
    print(f"А: {'==' * 10}{t.asctime()}{'==' * 10}\n")
    f.write(f"А: {'==' * 10}{t.asctime()}{'==' * 10}\n")
while True:


        r = requests.get('https://sociumin.com/?id=5160931')
        soup = BeautifulSoup(r.content, "lxml")
        mtime = soup.find("span").text
        if mtime != mlasttime:
            with open("result.txt", "a") as f:
                f.write(f"М: {mtime} : {t.asctime()}\n")
            print(f"М: {mtime} : {t.asctime()}\n")
        mlasttime = mtime

        t.sleep(0.01)
        continue
