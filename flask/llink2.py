# short link service
import requests


def get_short_link(link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': 'Bearer 3d3c4e4e4f1d4e2b4e4e4e4e4e4e4e4e4e4e4e4e',
        'Content-Type': 'application/json'
    }
    data = {
        'long_url': link
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


a=get_short_link('https://docs-python.ru/standart-library/modul-functools-python/ispolzovanija-modulja-functools/')
print(a)