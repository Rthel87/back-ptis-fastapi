from db.database import SessionLocal
from db import models
from sqlalchemyseed import load_entities_from_json, HybridSeeder

# Load entities
entities = load_entities_from_json('./seeders/seeder2.json')

# Initializing Seeder
session = SessionLocal()
seeder = HybridSeeder(session, ref_prefix='!')

# Seeding
seeder.seed(entities)

session.commit()
session.close()

#### Script for sqlalchemy-seeder ------ Don´t work


# from db.database import SessionLocal
# from db.models import Rol, Jornada, Semestre, Seccion, Curso, Usuario, Grupo
# from sqlalchemyseeder import ResolvingSeeder
# import yaml
# import json
#
# with open('./seeders/seeder.yml', 'r') as file:
#     configuration = yaml.safe_load(file)
# # with open('./seeders/seeder.json', 'r') as file:
# #     configuration = json.load(file)
# print(configuration)
# print(isinstance(configuration, list))
# print(isinstance(configuration[0], dict))
# # json_data = str(configuration).replace("'", '"')
# # print(json_data)
#
# # Load Seeder
# session = SessionLocal()
# seeder = ResolvingSeeder(session)
# # new_entities = seeder.load_entities_from_yaml_file("./seeders/seeder.yml")
# # new_entities = seeder.load_entities_from_json_file("./seeders/seeder.json")
# # new_entities = seeder.load_entities_from_json_string(str(json_data))
# new_entities = seeder.load_entities_from_data_dict(configuration)
# session.commit()
# session.close()
