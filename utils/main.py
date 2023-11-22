from db.database import SessionLocal
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
