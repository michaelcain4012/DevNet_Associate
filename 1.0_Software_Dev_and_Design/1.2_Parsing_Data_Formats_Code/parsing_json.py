import json
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'json_example.json')) as file:
    data = json.load(file) #Transforms json data into python dictionary
user = data['user']
print(user['name'])

for role in user['roles']:
    print(role)

user['location']['city'] = 'Dallas'
with open(os.path.join(here, 'json_example-edited.json'), 'w') as file:
    json.dump(data, file, indent=4) #Dumps python dictionary into json foramt, the indent parameter will make the file more readable
    