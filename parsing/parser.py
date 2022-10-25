import datetime
import time

import requests
import asyncio
from bs4 import BeautifulSoup




headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.673 Yowser/2.5 Safari/537.36"
}


link_selexy = f'https://salexy.kg'
post = requests.get(link_selexy, headers=headers)
postsrc = post.text


POSTSOUD = BeautifulSoup(postsrc, "lxml")
deteil_post_links = []

def get_category(POSTSOUD):
    perl = POSTSOUD.find(class_='nav-list').find_all('a')
    list_category_link = []
    list_cateory_name = []

    for i in perl:
        if len(i['href'].split('/')) == 4:

            list_category_link.append(i['href'])
            list_cateory_name.append(i.text)

    return list_category_link, list_cateory_name

#

current_datetime = datetime.datetime.now()
print(current_datetime)
list_category,list_name=get_category(POSTSOUD)
current_datetime = datetime.datetime.now()
print(current_datetime)

for i in list_name:
    print(*i.split()[1:])