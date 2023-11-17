from pydantic import BaseModel, EmailStr
from datetime import Date
from typing import Optional

# Definición de la clase Usuario con Pydantic
class UsuarioBase(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    run: str | None = None
    correo_elec: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    rol_id: int
    borrado: bool
    estudiante: Optional[Estudiante] = None
    profesor: Optional[Profesor] = None
    stakeholder: Optional[Stakeholder] = None

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

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


# Definición clase Profesor con Pydantic
class ProfesorBase(BaseModel):
    pass

class ProfesorCreate(ProfesorBase):
    pass

class Profesor(ProfesorBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True


# Definición clase Estudiante con Pydantic
class EstudianteBase(BaseModel):
    iniciales: str

class EstudianteCreate(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    id: int
    usuario_id: int
    grupo_id: int
    seccion_id: int

    class Config:
        orm_mode = True


# Definición clase Stakeholder con Pydantic
class StakeholderBase(BaseModel):
    iniciales: str

class StakeholderCreate(StakeholderBase):
    pass

class Stakeholder(StakeholderBase):
    id: int
    usuario_id: int
    grupos: list[Grupo] = []

    class Config:
        orm_mode = True


# Definición clase Grupo con Pydantic
class GrupoBase(BaseModel):
    nombre: str
    proyecto: str
    correlativo: int

class GrupoCreate(GrupoBase):
    pass

class Grupo(GrupoBase):
    id: int
    estudiantes: list[Estudiante] = []
    stakeholders: list[Stakeholder] = []

    class Config:
        orm_mode = True
