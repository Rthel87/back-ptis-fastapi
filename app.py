from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine
from typing import Union

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
## Creación de sesión de conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('/jornadas', response_model=list[schemas.Jornada])
def read_jornadas(db: Session = Depends(get_db)):
    jornadas = crud.get_jornadas(db)
    return jornadas
