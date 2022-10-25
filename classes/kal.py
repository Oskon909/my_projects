# url shorter
def urlshort(url):
    import requests
    import json
    api = "https://is.gd/create.php?format=json&url="
    r = requests.get(api+url)
    data = json.loads(r.text)
    print(data)
    # return data["shorturl"]


print(urlshort("http://youtube.com"))


