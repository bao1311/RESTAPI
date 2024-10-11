import requests
import json
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
# print("no")
list = response.json()['items']
for data in list:
    print(data['owner']['profile_image'])
