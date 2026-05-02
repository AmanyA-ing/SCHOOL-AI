from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

jour_cree= datetime.now().strftime("%Y")
fichier_nom=f"bosco{jour_cree}"
URL = f"sqlite:///./{fichier_nom}.db"
engine = create_engine(URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        