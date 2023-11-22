from .database import SessionLocal

# Sesión de base de datos para los distintos módulos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
