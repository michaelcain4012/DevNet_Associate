import yaml
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'yaml_example.yml')) as file:
    data = yaml.safe_load(file) #Transforms YAML file into python dictionary
user = data['user']
print(user['name'])

for role in user['roles']:
    print(role)

user['location']['city'] = 'Dallas'
with open(os.path.join(here, 'yaml_example-edited.yml'), 'w') as file:
    yaml.dump(data, file, default_flow_style=False) #Dumps python dictionary into YAML format
