from db.database import SessionLocal
from db import models
from sqlalchemyseed import load_entities_from_json, Seeder, HybridSeeder
from sqlalchemy import select, insert, update
from dotenv import dotenv_values
import bcrypt
# import pdb

env = dotenv_values(".env")

# Load entities
entities = load_entities_from_json('./seeders/seeder2.json')
# entities_with_ref = load_entities_from_json('./seeders/seeder_with_refs.json')

# Initializing Seeder
session = SessionLocal()
seeder = Seeder(session)

# Seeding entities without refs!
seeder.seed(entities)
session.commit()

# Seeding entities with refs
# hybrid = HybridSeeder(session, ref_prefix='!')
# breakpoint()
# hybrid.seed(entities_with_ref)
# session.commit()

# Generando password inicial para administrador y profesor
password = env["ADMIN_PW"].encode('UTF-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode('UTF-8')
admin = session.scalars(
    select(models.Usuario).where(models.Usuario.rol.has(models.Rol.rango == 1))
).one()

# Agregando secciones al profesor
stmt = select(models.Profesor).where(models.Profesor.usuario_id == 200)
profesor = session.scalars(stmt).one()
secciones_add = session.scalars(
    select(models.Seccion).where(models.Seccion.jornada.has(models.Jornada.identificador == 2))
).all()
for seccion in secciones_add:
    seccion.profesores.append(profesor)

# Actualizando password inicial a administrador y profesor
query = update(models.Usuario).where(models.Usuario.id.in_([admin.id, profesor.usuario_id])).values(password=hashed)
session.execute(query)

session.commit()

print(" --------------- Se han agregado las entidades a la base de datos ---------------")

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
