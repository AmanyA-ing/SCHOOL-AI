from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import models
from database import SessionLocal, engine
from passlib.context import CryptContext

app = FastAPI(title="BOSCO AI")

# Connexion à la base
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
