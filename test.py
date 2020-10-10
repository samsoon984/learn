from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import os
import sys

def get_url(number = int(input('품번 입력: '))):
    #while i <= 10:
    #    print("https://hitomi.la/reader/%d.html#%d"%(number,i))
    #    i+=1
    
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, 'html.parser')
    i = 1
    while i <= 1000:
        if i < 10:
            url = "https://cdn.hiyobi.me/data/%d/0%d.png"%(number,i)
            res = requests.get(url)
            if (res.status_code == 200):
                print(i)
                i += 1
            else:
                sys.exit()
        else:
            url = "https://cdn.hiyobi.me/data/%d/%d.png"%(number,i)
            res = requests.get(url)
            if (res.status_code == 200):
                print(i)
                i += 1
            else:
                sys.exit()
    
    #url1 = "https://github.com/samsoon984"
    #res = requests.get(url1)
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)

get_url()








