#There are a few ways to parse XML unfortunately. Only two techniques are really found in the test. 
#Both will be expllored here

import xml.etree.ElementTree as ET #defining this module as ET allows us to skip typing that long crap everytime. yay
import xmltodict
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'xml_example.xml'), 'r') as file:
    mytree = ET.parse(file) #Transforms XML file into python ElementTree instance
    myroot = mytree.getroot()
user = myroot.find('user')
print(user.find('name').text)

for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = 'Dallas'
with open(os.path.join(here, 'xml_example-edited.yml'), 'w') as file:
    mytree.write(file, encoding='unicode') #Dumps python ElementTree into XML format


# xmltodict approach (most similar to yaml and json parsing process)

with open(os.path.join(here, 'xml_example.xml')) as file:
    data = xmltodict.parse(file.read())['root'] #Transforms XML file into python dictionary
user = data['user']
print(user['name'])

for role in user['roles']:
    print(role)

user['location']['city'] = 'Dallas'
with open(os.path.join(here, 'xml_example-edited.xml'), 'w') as file:
    xmltodict.unparse(data, file, encoding='unicode') #Dumps python dictionary into YAML format
