import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': 'get your own'
}

response = requests.get(url, headers=headers).json()

print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['name'] == 'home':
        orgId = response_org['id']


print(orgId)