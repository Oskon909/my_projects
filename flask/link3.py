import hashlib
import redis


def short_url(url):
    hash_object = hashlib.md5(b'url')
    data = redis.Redis()
    data.mset({str(hash_object.hexdigest()): url})
    print(hash_object.hexdigest())
    return hash_object.hexdigest()

def get_link(object):
    data = redis.Redis()
    data_value = data.get(str(object.hexdigest()))
    print(data_value.decode('utf-8'),'<<<<<<<')



#
# short_url('https://docs-python.ru/standart-library/modul-functools-python/ispolzovanija-modulja-functools/')
get_link('572d4e421e5e6b9bc11d815e8a027112')