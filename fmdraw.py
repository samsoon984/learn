import requests
import random
from bs4 import BeautifulSoup

#test url: https://www.fmkorea.com/3266529210

url = input("url 입력( 예시: https://www.fmkorea.com/123456 ): ")
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
getComments = soup.select('#cmtPosition > ul')
find = soup.find('ul', {'class' :'fdb_lst_ul'}).find_all('a', {'href' :'#popup_menu_area'})
cutOverlap = list(set(find))
listnum = 0
print('----------------------------------')
for i in cutOverlap:
    print(cutOverlap[listnum].text)
    listnum += 1
print('----------------------------------')
print(f"총 {listnum}명, 당첨자: {random.choice(cutOverlap).text}")
print('----------------------------------')
