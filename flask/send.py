# @app.task
# def send_data_to_fapi_service():
#     url = 'fapi_service_url'
#     adverts_count = Advertisement.objects.count()
#     start_slice = 0
#     stop_slice = 100
#
#     for i in range(adverts_count):
#         if start_slice <= len(adverts_count):
#             break
#         # [start_slice: stop_slice]
#         # requests.post(url, AdvertisementSerializer(Advertisement.objects.query(
#         #     "SELECT * FROM advert "
#         # ), many=True))
#         start_slice = stop_slice
#         stop_slice += 100
import requests

response=requests.get('http://127.0.0.1:5000/get', json={'name': 'test', 'description': 'test dkavc jd qjebcbd', 'from_price': 1000,
                                                              'email ': 1, 'owner': 1, 'image': 'test',
                                                              'wa_number':'0247238','category': 1, 'subcategory': 1,'city': 1})
print(response.json())

# response=requests.get('http://127.0.0.1:5000/get_data', json={'kali':1000})