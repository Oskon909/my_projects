import json


a={"shorturl": "https://is.gd/1Z7X4D", "url": "http://youtube.com", "title": "YouTube", "status": "ok"}
print(type(a))
y=json.dumps(a)

print(type(y))