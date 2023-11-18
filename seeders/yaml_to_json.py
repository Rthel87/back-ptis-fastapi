import yaml
import json

with open('./seeders/seeder.yml', 'r') as file:
    configuration = yaml.safe_load(file)

with open('./seeders/seeder2.json', 'w') as json_file:
    json.dump(configuration, json_file)

output = json.dumps(json.load(open('./seeders/seeder.json')), indent=2)
print(output)
