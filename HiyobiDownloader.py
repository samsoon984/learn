from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import os
import sys

def get_url(number = int(input('품번 입력: '))):
    #while i <= 10:
    #    print("https://hitomi.la/reader/%d.html#%d"%(number,i))
    #    i+=1
    #url1 = "https://hiyobi.me/reader/%d#1"%number
    i = 1
    path1 = "C:/Bitnami/wampstack-7.4.10-0/apache2/htdocs/learn/%s"%number
    path2 = "C:/Bitnami/wampstack-7.4.10-0/apache2/htdocs/learn"
    try:
        if not(os.path.isdir("%s"%number)):
            os.makedirs(os.path.join("%s"%number))
            print("making directory..")
    except:
        print("error!!!")
    while i <= 1000:
        if i < 10:
            if os.path.isdir("%s"%number):
                url = "https://cdn.hiyobi.me/data/%d/0%d.jpg"%(number,i)
                res = requests.get(url)
                print(res.status_code)
                if (res.status_code == 200):
                    os.chdir(path1)
                    file = open("%s.png"%i,"wb")
                    file.write(res.content)
                    file.close()
                    print(url)
                    os.chdir(path2)
                    i += 1
                else:
                    sys.exit()
        else:
            if os.path.isdir("%s"%number):
                url = "https://cdn.hiyobi.me/data/%d/%d.jpg"%(number,i)
                res = requests.get(url)
                print(res.status_code)
                if (res.status_code == 200):
                    os.chdir(path1)
                    file = open("%s.png"%i,"wb")
                    file.write(res.content)
                    file.close()
                    print(url)
                    os.chdir(path2)
                    i += 1
                else:
                    sys.exit()


    #url1 = "https://github.com/samsoon984"
    #res = requests.get(url1)
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)

get_url()








