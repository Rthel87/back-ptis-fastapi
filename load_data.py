from db.database import SessionLocal
from sqlalchemyseeder import ResolvingSeeder
import yaml
import json

with open('./seeders/seeder.yml', 'r') as file:
    configuration = yaml.safe_load(file)
print(configuration)
print(isinstance(configuration, list))
print(isinstance(configuration[0], dict))
# json_data = str(configuration).replace("'", '"')
# print(json_data)

# Load Seeder
session = SessionLocal()
seeder = ResolvingSeeder(session)
# new_entities = seeder.load_entities_from_yaml_file("./seeders/seeder.yml")
# new_entities = seeder.load_entities_from_json_file("./seeders/seeder.json")
# new_entities = seeder.load_entities_from_json_string(str(json_data))
new_entities = seeder.load_entities_from_data_dict(configuration)
session.commit()
session.close()
