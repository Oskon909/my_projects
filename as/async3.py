import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.673 Yowser/2.5 Safari/537.36"
}
# asynchronous parsing
async def get_post(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link, headers=headers) as response:
            return await response.text()

async def get_post_links(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link, headers=headers) as response:
            return await response.text()

def get_category(POSTSOUD):
    perl = POSTSOUD.find(class_='nav-list').find_all('a')
    list_category_link = []
    list_cateory_name = []

    for i in perl:
        if len(i['href'].split('/')) == 4:
            list_category_link.append(i['href'])
            list_cateory_name.append(i.text)

    return list_category_link, list_cateory_name


async def main():
    link_selexy = f'https://salexy.kg'
    post = await get_post(link_selexy)
    postsrc = post

    POSTSOUD = BeautifulSoup(postsrc, "lxml")
    deteil_post_links = []

    list_category_link, list_cateory_name = get_category(POSTSOUD)
    for i in list_category_link:
        post = await get_post_links(i)
        postsrc = post
        POSTSOUD = BeautifulSoup(postsrc, "lxml")
        perl = POSTSOUD.find_all(class_='product-name')
        for i in perl:
            deteil_post_links.append(i['href'])
    return deteil_post_links

if __name__ == '__main__':
    a=asyncio.run(main())
    print(a)
