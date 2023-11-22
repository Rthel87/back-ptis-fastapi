from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db import models, schemas, crud
from db.session import get_db
from pydantic import BaseModel
from dotenv import dotenv_values
import bcrypt
import jwt

router = APIRouter()

env = dotenv_values(".env")

class Data(BaseModel):
    email: str
    password: str

class Auth(BaseModel):
    auth: Data

@router.post("/auth/login")
def login(auth: Auth, db: Session = Depends(get_db)):
    usuario = crud.get_usuario_by_email(db, auth.auth.email)
    if usuario is None:
        return {"error": "Usuario no autorizado"}
    if bcrypt.checkpw(auth.auth.password.encode("UTF-8"), usuario.password.encode("UTF-8")) is not True:
        return {"error": "Contraseña errónea"}
    token = jwt.encode({"usuario_id": usuario.id}, env["SECRET_WORD"], algorithm="HS256")
    return {"jwt": token}
