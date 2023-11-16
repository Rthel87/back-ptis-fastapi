from pydantic import BaseModel
from datetime import Date

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


# Definición clase Rol con Pydantic
class RolBase(BaseModel):
    rol: str
    rango: int

class RolCreate(RolBase):
    pass

class Rol(RolBase):
    id: int
    usuarios: list[Usuario] = []
    borrado: bool

    class Config:
        orm_mode = True


# Definición clase Seccion con Pydantic
class SeccionBase(BaseModel):
    codigo: str

class SeccionCreate(SeccionBase):
    pass

class Seccion(SeccionBase):
    id: int
    curso_id: int
    jornada_id: int
    semestre_id: int
    borrado: bool


# Definición clase Jornada con Pydantic
class JornadaBase(BaseModel):
    nombre: str
    identificador: int

class JornadaCreate(JornadaBase):
    pass

class Jornada(JornadaBase):
    id: int
    secciones: list[Seccion] = []
    borrado: bool


# Definición clase Semestre con Pydantic
class SemestreBase(BaseModel):
    numero: int
    agno: int
    activo: bool
    inicio: Date
    fin: Date

class SemestreCreate(SemestreBase):
    identificador: str = str(agno) + '-' + str(numero)

class Semestre(SemestreBase):
    id: int
    identificador: str
    secciones: list[Seccion] = []
    borrado: bool


# Definición clase Curso con Pydantic
class CursoBase(BaseModel):
    nombre: str
    codigo: str

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    secciones: list[Seccion] = []
    borrado: bool
