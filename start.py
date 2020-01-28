import requests
from bs4 import BeautifulSoup
import os
import random
import time
import re

# Choose the needed one!
# def clear(): return os.system('cls')  # on Windows System
clear = lambda: os.system('clear') # on Linux System

count = 0
onebar = "|"
bar = ""
api_checker = "https://surfheaven.eu/map/"

with open(r'maps.txt') as f:
    content = f.readlines()

for i in content:
    time.sleep(0.9)
    maps = i
    maps = maps.replace("./", "")
    maps = maps.replace(".bsp", "")
    maps = re.sub("[^a-z0-9_-]+","", maps, flags=re.IGNORECASE)
    URL = api_checker + maps

    if count % 15 == 0:
        bar += onebar
        
    count = count + 1
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    mydivs = soup.findAll("div", class_="container-fluid")
    mydivs2 = soup.findAll("strong", class_="c-white")

    for last_div in mydivs:pass
    
    if last_div:
        error = last_div.getText()
        error = error.strip()

    if error == "Unable to find map..":
        simple = "Tier: %s | Type: %s | Map: %s\n" % ("N/A", "UNKNOWN", str(maps))
    else:
        tier = mydivs2[2].getText()
        mode = mydivs2[3].getText()
        if mode == "Staged":
            modetext = "Stages"
            modewrite = mydivs2[5].getText()
        else:
            modetext = "Checkpoints"
            modewrite = mydivs2[5].getText()
        simple = "Tier: %s | Type: %s | %s: %s | Map: %s\n" % (tier, mode, modetext ,modewrite, str(maps))

    f = open("completed.txt", "a+")
    clear()
    f.write(simple)
    f.close()
    print("Loading.. \nCurrent line: " + str(count) +"\n" + bar)
    

print(str(count) + " maps checked with surfheavens database.\nProject made by Dovydev [github.com/dovydev]") 
