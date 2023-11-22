from db.database import SessionLocal

# Dependency
## Creación de sesión de conexión a la base de datos

# Sesión de base de datos para los distintos módulos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
