from typing import Annotated
from fastapi import Depends, APIRouter, Header
from sqlalchemy.orm import Session
from db import models, schemas, crud
from utils.main import get_db, encode_token, current_usuario
from pydantic import BaseModel
import bcrypt

router = APIRouter()

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
    token = encode_token({"usuario_id": usuario.id})
    return {"jwt": token}

@router.get("/login/user", response_model=schemas.Usuario)
def user(authorization: Annotated[str | None, Header()] = None, db: Session = Depends(get_db)):
    return current_usuario(authorization, db)
