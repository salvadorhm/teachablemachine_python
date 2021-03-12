import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:8080'
payload = {"image": open('keyboard2.jpg', 'rb')}

'''
Authorization with user and pass
'''
auth = HTTPBasicAuth("user","pass")
headers = {"Authorization": auth}
response = requests.post(url, files = payload, auth = auth)

'''
Authorization with a token
'''
# token = "1234"
# headers = {"Authorization": token}
# response = requests.post(url, files=payload, headers=headers)
print(response.text)
