import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser" : {
        "attributes" : {
            "name" : "admin",
            "pwd" : "ciscopsdt"
        }
    }
}

headers = {
    'Content-Type' : "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

# Parse token and set cookie
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

########## GET APN ##########
# Get app profile
url = "https://sandboxapidc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

headers = {
    'cache-control' : "no-cache"
}

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()


print(json.dumps(get_response, indent=2, sort_keys=True))

########## UPDATE APN DESCRIPTION #########
# Set description
post_payload = {
    "fvAp" : {
        "attributes": {
            "descr" : " ",
            "dn" : "uni/tn-Heroes/ap-save_The_Planet"
        }
    }
}

post_response = requests.post(
    url, headers=headers, cookies=cookie, verify=False, data=json.dumps(post_payload)).json()

get_response = requests.get(url,headers=headers,cookies=cookie, verify=False).json()

print(json.dumps(get_response,indent=2, sort_keys=True))