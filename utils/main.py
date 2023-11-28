from sqlalchemy.orm import Session
from db.database import SessionLocal
from db import models
from dotenv import dotenv_values
import jwt

env = dotenv_values(".env")

# Dependency
## Creación de sesión de conexión a la base de datos
# Sesión de base de datos para los distintos módulos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def encode_token(payload):
    return jwt.encode(payload, env["SECRET_WORD"], algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, env["SECRET_WORD"], algorithms=["HS256"])

def get_id_from_header(header: str):
    token = header.split(' ')[1]
    payload = decode_token(token)
    return payload["usuario_id"]

def current_usuario(header: str, db: Session):
    user_id = get_id_from_header(header)
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
