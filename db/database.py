from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

env_values = dotenv_values(".env")

# SQLALCHEMY_DATABASE_URL = "sqlite:///./ptis_back.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgreserver/db"
# SQLALCHEMY_DATABASE_URL = "postgresql://" + env_values["PG_USER"] + ":" + env_values["PG_PASSWORD"] + "@" + env_values["PG_HOST"] + "/" + env_values["PG_DBASE"]
SQLALCHEMY_DATABASE_URL = env_values["DB_URL"]

engine = create_engine(
    SQLALCHEMY_DATABASE_URL #,
    # connect_args = {"check_same_thread": False}  # Argumento necesario solamente en SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
