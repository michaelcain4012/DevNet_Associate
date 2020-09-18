Netfonf protocol is how computer and network device can talk to each another
- uses ssh, tcp, authen, encryption, port 830, passes XML data

1. Get operational state of device (vlan status, int status)
2. get configuation state
3. Edit configuration (this is where SNMP lacked)

NX-API
to enable on device just use "feature nxapi" command
to enable sandbox do "nxapi sandbox"
2 versions
1. nx-api CLI
  - Over HTTP/https
  - can only use POST
  - you are basically posting CLI commands

  import requests
  import json

  url = "https://sbx-nxos-mgmt.cisco.com/ins"
  switchuser = "admin"
  switchpassword = "Admin_1234!"

  myheaders = {"content-type": "application/json"}
  payload = {
      "ins_api": {
          "version": "1.0",
          "type": "cli_show",
          "chunk": "0",
          "sid": "1",
          "input": "show ip int brief",
          "output_format": "json",
      }
  }
  response = requests.post(
      url,
      data=json.dumps(payload),
      headers=myheaders,
      auth=(switchuser, switchpassword),
      verify=False,
  ).json()

  print(json.dumps(response, indent=2, sort_keys=True))

2. NX-API REST
- uses the object model
- Data management engine in nexus handles all requests
- DME uses the Manaagement info tree
- objects have 2 names the relative name (just the file name) and the distinguished name (file name with path)
