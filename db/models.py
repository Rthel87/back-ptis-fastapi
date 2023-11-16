from sqlalchemy import Boolean, Column, ForeignKey, BigInteger, Integer, String, DateTime, text
from sqlalchemy.orm import relationship

from .database import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(BigInteger, primary_key=True, index=True)
    rol = Column(String, index=True)
    rango = Column(Integer, unique=True, index=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    usuarios = relationship("Usuario", back_populates="rol")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido_paterno = Column(String, index=True)
    apellido_materno = Column(String, index=True)
    run = Column(String, index=True)
    correo_elec = Column(String, unique=True, index=True)
    password = Column(String)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    rol = relationship("Rol", back_populates="usuarios")

class Jornada(Base):
    __tablename__ = "jornadas"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, index=True)
    identificador = Column(Integer, unique=True, index=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    secciones = relationship("Seccion", back_populates="jornada")

class Semestre(Base):
    __tablename__ = "semestres"

    id = Column(BigInteger, primary_key=True, index=True)
    numero = Column(Integer, index=True)
    agno = Column(Integer, index=True)
    identificador = Column(String, unique=True, index=True)
    activo = Column(Boolean, default=True)
    inicio = Column(Date)
    fin = Column(Date)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    secciones = relationship("Seccion", back_populates="semestre")

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, index=True)
    codigo = Column(String, unique=True, index=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    secciones = relationship("Seccion", back_populates="curso")

class Seccion(Base):
    __tablename__ = "secciones"

    id = Column(BigInteger, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    jornada = relationship("Jornada", back_populates="secciones")
    semestre = relationship("Semestre", back_populates="secciones")
    curso = relationship("Curso", back_populates="secciones")
    profesores = relationship("Profesor", back_populates="secciones")

class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(BigInteger, primary_key=True, index=True)

    usuario = relationship("Usuario", back_populates="profesor")
    secciones = relationship("Seccion", back_populates="profesores")
