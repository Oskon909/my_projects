import requests

response=requests.post('http://127.0.0.1:5000/get_data')
print(response.json())