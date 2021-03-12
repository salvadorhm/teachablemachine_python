import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:8080'
payload = {"image": open('keyboard2.jpg', 'rb')}
# headers = {"Authorization": "1234"}
auth = HTTPBasicAuth("user","pass")
headers = {"Authorization": auth}
# response = requests.post(url, files=payload, auth = auth)
response = requests.post(url, files=payload, auth = ("user","pass"))
# response = requests.post(url, files=payload, headers=headers)
print(response.text)
