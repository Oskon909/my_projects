import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

URL = 'https://salexy.kg'


class Api:
    def __init__(self, url: str):
        self.url = url

    def http_get(self, times: int):
        content = []
        for _ in tqdm(range(times), desc='Fetching data...', colour='GREEN'):
            response = requests.get(self.url)
            response=response.text
            post=BeautifulSoup(response, "lxml")
            perl = post.find(class_='nav-list').find_all('a')
            list_category_link = []
            list_cateory_name = []

            for i in perl:
                if len(i['href'].split('/')) == 4:
                    list_category_link.append(i['href'])
                    list_cateory_name.append(i.text)

            return list_category_link, list_cateory_name


if __name__ == '__main__':
    N = 10
    api = Api(URL)

    start_timestamp = time.time()
    print(api.http_get(times=N))
