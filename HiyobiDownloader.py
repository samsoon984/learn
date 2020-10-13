import requests
import os
import sys
import time
import random


start = time.time()

def get_url(number = str(input('품번 입력: '))):
    try:
        if not(os.path.isdir(number)):
            os.makedirs(os.path.join(number))
            print("making directory..")
    except:
        print("already exist..")
    i = 1
    while i <= 1000:
        url = f"https://cdn.hiyobi.me/data/{number}/{str(i).zfill(2)}.jpg"
        res = requests.get(url)
        print(url)
        print(res.status_code)
        if (res.status_code == 200):
            with open(f"{number}/{i}.jpg", "wb") as f:
                f.write(res.content)
            i += 1
            print("sleep,,, this is not error")
            time.sleep( random.uniform(0.5,1) )
        else:
            print("time :", time.time() - start)
            sys.exit()
    
get_url()


