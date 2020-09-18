import meraki
import json
from pprint import pprint

token = '1c4bd6d02f96aeeb9426bc6b13756e7cf8fb57b0'
orgNameCheck = 'home' #this is the organization name within meraki dashboard
networkNameCheck = 'Michael_Cain'
dashboard = meraki.DashboardAPI(token)

orgs = dashboard.organizations.getOrganizations()
pprint(orgs) 

for org in orgs:
    if org['name'] == orgNameCheck:
        orgId = org['id']

print(orgId)

params = {}
params['organization_id'] = orgId
networks = dashboard.organizations.getOrganizationNetworks(orgId)
pprint(networks)

#for network in networks:
#    if network['name'] == networkNameCheck:
#        netId = nework['id']
#
#vlans = dashboard.networks.getNetworkVlans(netId)
#pprint(vlans)


