import requests
from bs4 import BeautifulSoup
import lxml
import json
import re
import time as t


alasttime = ""
with open("result.txt", "a") as f:
    print(f"А: {'=='*10}{t.asctime()}{'=='*10}\n")
    f.write(f"А: {'=='*10}{t.asctime()}{'=='*10}\n")

while True:
    
    r = requests.get('https://sociumin.com/?id=950757')
    soup = BeautifulSoup(r.content, "lxml")
    atime = soup.find("span").text
    if atime != alasttime:
        with open("result.txt", "a") as f:
            f.write(f"А: {atime} :{t.asctime()}\n")
        print(f"А: {atime} : {t.asctime()}\n")
    alasttime = atime

    t.sleep(0.01)
    continue