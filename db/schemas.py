from pydantic import BaseModel

# Definición clase Rol con Pydantic
class RolBase(BaseModel):
    rol: str
    rango: int

class RolCreate(RolBase):
    pass

class Rol(RolBase):
    id: int
    usuarios: list[Rol] = []
    borrado: bool

    class Config:
        orm_mode = True

# Definición de la clase Usuario con Pydantic
class UsuarioBase(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    run: str | None = None
    correo_elec: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    rol_id: int
    borrado: bool

    class Config:
        orm_mode = True
