import enum
from sqlalchemy import Column, Integer, String, Enum, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

#Class pour option
class Genre(enum.Enum):
    MASCULIN = "Masculin"
    FEMININ = "Féminin"

# Class original
class Trimestre(Base):
    __tablename__ = "trimestre"
    id = Column(Integer, primary_key=True, index=True)
    nom_trimestre = Column(String)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)

class Professeur(Base):
    __tablename__ = "professeur"
    id = Column(Integer, primary_key=True, index=True)
    genre_professeur = Column(Enum(Genre), default=Genre.MASCULIN, nullable=False)
    nom_professeur = Column(String, unique=True, index=True)
    nom_matiere = Column(String)
    
class Classe(Base):
    __tablename__ = "Classe"
    id = Column(Integer, primary_key=True, index=True)
    nom_classe = Column(String)
    nombre_effectif = Column(Integer)

class Feuille(Base):
    __tablename__ = "Type de feuille"
    id = Column(Integer, primary_key=True, index=True)
    nom_feuille = Column(String)
    marque_feuille= Column(Integer,default="feuille simple")

class Gestion(Base):
    __tablename__ = "Gestion des feuilles"
    id = Column(Integer, primary_key=True, index=True)
    nom_professeur = Column(String, unique=True, index=True)
    nom_matiere=Column(String)
    nom_classe = Column(String)
    nom_feuille = Column(String)
    nombre_feuille = Column(Integer)
    nom_trimestre = Column(String)
    date=Column(String, default=datetime.now)
