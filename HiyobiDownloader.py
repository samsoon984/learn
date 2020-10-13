from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import os
import sys
import time
import random


i = 1

start = time.time()

def get_url(number = int(input('품번 입력: '))):
    path1 = "./%s"%number
    path2 = "../"
    def get_num(q = int):
        global i
        url = "https://cdn.hiyobi.me/data/%d/%s%d.jpg"%(number,q,i)
        res = requests.get(url)
        print(url)
        print(res.status_code)
        if (res.status_code == 200):
            os.chdir(path1)
            file = open("%s.png"%i, "wb")
            file.write(res.content)
            file.close()
            os.chdir(path2)
            i += 1
            print("sleep,,, this is not error")
            time.sleep( random.uniform(0.5,1) )
        else:
            print("time :", time.time() - start)
            sys.exit()
    #while i <= 10:
    #    print("https://hitomi.la/reader/%d.html#%d"%(number,i))
    #    i+=1
    #url1 = "https://hiyobi.me/reader/%d#1"%number
    try:
        if not(os.path.isdir("%s"%number)):
            os.makedirs(os.path.join("%s"%number))
            print("making directory..")
    except:
        print("error!!!")
    while i <= 1000:
        if i < 10:
            if os.path.isdir("%s"%number):
                get_num("0")
        else:
            if os.path.isdir("%s"%number):
                get_num("")


    #url1 = "https://github.com/samsoon984"
    #res = requests.get(url1)
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)




get_url()


