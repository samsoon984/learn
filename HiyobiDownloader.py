from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import os


def get_url(number = int(input('품번 입력: ')), page = int(input('쪽수 입력: '))):
    #while i <= 10:
    #    print("https://hitomi.la/reader/%d.html#%d"%(number,i))
    #    i+=1
    #url1 = "https://hiyobi.me/reader/%d#1"%number
    i = 1
    #path = "C:/Bitnami/wampstack-7.4.10-0/apache2/htdocs/learn/%s"%number
    try:
        if not(os.path.isdir("%s"%number)):
            os.makedirs(os.path.join("%s"%number))
            print("making directory..")
    except:
        print("error!!!")
    while i <= page:
        if i < 10:
            if os.path.isdir("%s"%number):
                url = "https://cdn.hiyobi.me/data/%s/0%s.png"%(number,i)
                res = requests.get(url)
                file = open("%s.png"%i,"wb")
                file.write(res.content)
                file.close()
                print(url)
                i += 1
        else:
            if os.path.isdir("%s"%number):
                url = "https://cdn.hiyobi.me/data/%s/%s.png"%(number,i)
                res = requests.get(url)
                file = open("%s.png"%i,"wb")
                file.write(res.content)
                file.close()
                print(url)
                i += 1


    #url1 = "https://github.com/samsoon984"
    #res = requests.get(url1)
    #res.raise_for_status()
    #soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup)

get_url()








