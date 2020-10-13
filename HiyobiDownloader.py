#from bs4 import BeautifulSoup
#from html.parser import HTMLParser
import requests
import os
import sys
import time
import random


start = time.time()

def get_url(number = int(input('품번 입력: '))):
    try:
        if not(os.path.isdir(f"{number}")):
            os.makedirs(os.path.join(f"{number}"))
            print("making directory..")
    except:
        print("already exist..")
    os.chdir(f"./{number}")
    i = 1
    while i <= 1000:
        url = f"https://cdn.hiyobi.me/data/{number}/{str(i).zfill(2)}.jpg"
        res = requests.get(url)
        print(url)
        print(res.status_code)
        if (res.status_code == 200):
            with open(f"{i}.jpg", "wb") as f:
                f.write(res.content)
            f.close()
            i += 1
            print("sleep,,, this is not error")
            time.sleep( random.uniform(0.5,1) )
        else:
            print("time :", time.time() - start)
            sys.exit()
    
get_url()


