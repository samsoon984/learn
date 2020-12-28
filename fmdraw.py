import requests
import random
from bs4 import BeautifulSoup

#test url: https://www.fmkorea.com/3283165045

url = input("url 입력( 예시: https://www.fmkorea.com/123456 ): ")
if 'best' in url:
    url = url.replace('/best','')
elif 'https://www.fmkorea.com/' not in url:
    url = f'https://www.fmkorea.com/{url}'
urlNum = url.replace('https://www.fmkorea.com/','')
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
find = []
if soup.find('strong', {'class': 'this'}).text != '1':
    for i in range(1, int(soup.find('strong', {'class': 'this'}).text)+1):
        commentUrl = f'https://www.fmkorea.com/index.php?document_srl={urlNum}&cpage={i}#{urlNum}_comment'
        soup = BeautifulSoup(requests.get(commentUrl).text, 'html.parser')
        find += soup.find('ul', {'class' :'fdb_lst_ul'}).find_all('a', {'href' :'#popup_menu_area'})
cutOverlap = list(set(find))
listnum = 0
print('----------------------------------')
for i in cutOverlap:
    print(cutOverlap[listnum].text)
    listnum += 1
print('----------------------------------')
print(f"총 {listnum}명, 당첨자: {random.choice(cutOverlap).text}")
print('----------------------------------')
