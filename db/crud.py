from sqlalchemy.orm import Session
from . import models, schemas

# Funciones CRUD para el modelo 'Usuario'
## Create
def create_usuario(db: Session, user: schemas.UsuarioCreate, role_id: int):
    fake_hashed_password = user.password + 'notReallyHashed'
    db_user = models.User(nombre=user.nombre, apellido_paterno=user.apellido_paterno, apellido_materno=user.apellido_materno, run=user.run, correo_elec=user.correo_elec, password=fake_hashed_password, rol_id=role_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

## Read
def get_usuario(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()

def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.correo_elec == email).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()


# Funciones CRUD para el modelo 'Rol'
## Create
def create_rol(db: Session, role: schemas.RolCreate):
    db_rol = models.Rol(rol=role.rol, rango=role.rango)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

## Read
def get_rol(db: Session, rol_id: int):
    return db.query(models.Rol).filter(models.Rol.id == rol_id).first()

def get_rol_by_rango(db: Session, rango: int):
    return db.query(models.Rol).filter(models.Rol.rango == rango).first()

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rol).offset(skip).limit(limit).all()
