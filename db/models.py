from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    rol = Column(String, index=True)
    rango = Column(Integer, index=True)
    borrado = Column(Boolean, default=False)

    usuarios = relationship("Usuario", back_populates="rol")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido_paterno = Column(String, index=True)
    apellido_materno = Column(String, index=True)
    run = Column(String, index=True)
    correo_elec = Column(String, index=True)
    password = Column(String)
    borrado = Column(Boolean, default=False)

    rol = relationship("Rol", back_populates="usuarios")
