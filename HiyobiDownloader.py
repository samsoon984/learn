from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests





def get_url(number = int(input('품번 입력: '))):
    #while i <= 10:
    #    print("https://hitomi.la/reader/%d.html#%d"%(number,i))
    #    i+=1
    url = "https://hiyobi.me/reader/%d.html#1"%number
    #url1 = "https://github.com/samsoon984"
    res = requests.get(url=url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)

get_url()








