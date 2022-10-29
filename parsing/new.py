import os
import datetime
import boto3
import urllib.request
import requests

from bs4 import BeautifulSoup
from tqdm import tqdm
import asyncio
import time

import aiohttp
import requests
from tqdm import tqdm


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.673 Yowser/2.5 Safari/537.36"
}

def get_category(POSTSOUD):
    perl = POSTSOUD.find(class_='nav-list').find_all('a')
    list_category_link = []
    list_cateory_name = []

    for i in perl:
        if len(i['href'].split('/')) == 4:
            list_category_link.append(i['href'])
            list_cateory_name.append(i.text)

    return list_category_link, list_cateory_name




async def run_pars_selexy():
    count_post = 0
    link_selexy = f'https://salexy.kg'
    async with aiohttp.ClientSession() as session:
        async with session.get(link_selexy, headers=headers) as response:
            postsrc = await response.text()
            POSTSOUD = BeautifulSoup(postsrc, "lxml")
            list_category_link, list_cateory_name = get_category(POSTSOUD)
            print(list_category_link)



            for i in list_category_link:
                async with session.get(i, headers=headers) as response:
                    postsrc = await response.text()







if __name__ == '__main__':
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    # run_pars_selexy()
    asyncio.run(run_pars_selexy())
    current_datetime = datetime.datetime.now()
    print(current_datetime)