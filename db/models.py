from sqlalchemy import Boolean, Column, ForeignKey, BigInteger, Integer, String, Date, DateTime, text, Table
from sqlalchemy.orm import relationship

from .database import Base

# Relaciones Many to Many
secciones_profesores = Table(
    "secciones_profesores",
    Base.metadata,
    Column("profesor_id", ForeignKey("profesores.id"), primary_key=True),
    Column("seccion_id", ForeignKey("secciones.id"), primary_key=True)
)

grupos_stakeholders = Table(
    "grupos_stakeholders",
    Base.metadata,
    Column("grupo_id", ForeignKey("grupos.id"), primary_key=True),
    Column("stakeholder_id", ForeignKey("stakeholders.id"), primary_key=True)
)


class Rol(Base):
    __tablename__ = "roles"

    id = Column(BigInteger, primary_key=True, index=True)
    rol = Column(String, index=True)
    rango = Column(Integer, unique=True)
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
    correo_elec = Column(String, unique=True)
    password = Column(String)
    rol_id = Column(BigInteger, ForeignKey("roles.id"))
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'))
    updated_at = Column(DateTime, server_default=text('NOW()'))
    deleted_at = Column(DateTime)

    rol = relationship("Rol", back_populates="usuarios")
    estudiante = relationship("Estudiante", back_populates="usuario")
    profesor = relationship("Profesor", back_populates="usuario")
    stakeholder = relationship("Stakeholder", back_populates="usuario")

class Jornada(Base):
    __tablename__ = "jornadas"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, index=True)
    identificador = Column(Integer, unique=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    deleted_at = Column(DateTime)

    secciones = relationship("Seccion", back_populates="jornada")

class Semestre(Base):
    __tablename__ = "semestres"

    id = Column(BigInteger, primary_key=True, index=True)
    numero = Column(Integer, index=True)
    agno = Column(Integer, index=True)
    identificador = Column(String, unique=True)
    activo = Column(Boolean, default=True)
    inicio = Column(Date)
    fin = Column(Date)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    deleted_at = Column(DateTime)

    secciones = relationship("Seccion", back_populates="semestre")

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, index=True)
    codigo = Column(String, unique=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    deleted_at = Column(DateTime)

    secciones = relationship("Seccion", back_populates="curso")

class Seccion(Base):
    __tablename__ = "secciones"

    id = Column(BigInteger, primary_key=True, index=True)
    codigo = Column(String, unique=True)
    borrado = Column(Boolean, default=False)
    jornada_id = Column(BigInteger, ForeignKey("jornadas.id"))
    semestre_id = Column(BigInteger, ForeignKey("semestres.id"))
    curso_id = Column(BigInteger, ForeignKey("cursos.id"))
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    deleted_at = Column(DateTime)

    jornada = relationship("Jornada", back_populates="secciones")
    curso = relationship("Curso", back_populates="secciones")
    semestre = relationship("Semestre", back_populates="secciones")
    profesores = relationship("Profesor", secondary=secciones_profesores, back_populates="secciones")
    estudiantes = relationship("Estudiante", back_populates="seccion")

class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(BigInteger, primary_key=True, index=True)
    usuario_id = Column(BigInteger, ForeignKey("usuarios.id"))
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)

    usuario = relationship("Usuario", back_populates="profesor")
    secciones = relationship("Seccion", secondary=secciones_profesores, back_populates="profesores")

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(BigInteger, primary_key=True, index=True)
    iniciales = Column(String, index=True)
    usuario_id = Column(BigInteger, ForeignKey("usuarios.id"))
    grupo_id = Column(BigInteger, ForeignKey("grupos.id"))
    seccion_id = Column(BigInteger, ForeignKey("secciones.id"))
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)

    usuario = relationship("Usuario", back_populates="estudiante")
    grupo = relationship("Grupo", back_populates="estudiantes")
    seccion = relationship("Seccion", back_populates="estudiantes")

class Grupo(Base):
    __tablename__ = "grupos"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String, index=True)
    proyecto = Column(String)
    correlativo = Column(Integer, index=True)
    borrado = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    deleted_at = Column(DateTime)

    estudiantes = relationship("Estudiante", back_populates="grupo")
    stakeholders = relationship("Stakeholder", secondary=grupos_stakeholders, back_populates="grupos")

class Stakeholder(Base):
    __tablename__ = "stakeholders"

    id = Column(BigInteger, primary_key=True, index=True)
    iniciales = Column(String, index=True)
    usuario_id = Column(BigInteger, ForeignKey("usuarios.id"))
    created_at = Column(DateTime, server_default=text('NOW()'), nullable=False)
    updated_at = Column(DateTime, server_default=text('NOW()'), nullable=False)

    usuario = relationship("Usuario", back_populates="stakeholder")
    grupos = relationship("Grupo", secondary=grupos_stakeholders, back_populates="stakeholders")
