import enum
from sqlalchemy import Column, Integer, String, Enum, Float, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

#Class pour option
class Genre(enum.Enum):
    MASCULIN = "Masculin"
    FEMININ = "Féminin"

# Class original
class Trimestre(Base):
    __tablename__ = "trimestre/semestre"
    id = Column(Integer, primary_key=True, index=True)
    nom_trimestre = Column(String)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)

class Professeur(Base):
    __tablename__ = "professeur"
    id = Column(Integer, primary_key=True, index=True)
    genre_professeur = Column(Enum(Genre), default=Genre.MASCULIN, nullable=False)
    nom_professeur = Column(String(50), unique=True, index=True)
    nom_matiere = Column(String)
    
class Classe(Base):
    __tablename__ = "Classe"
    id = Column(Integer, primary_key=True, index=True)
    nom_classe = Column(String, unique=True, nullable=False)
    nombre_effectif = Column(Integer,default=38, nullable=False)

class Materiel(Base):
    __tablename__ = "matériel"
    id = Column(Integer, primary_key=True, index=True)
    nom_materiel = Column(String, unique=True,nullable=False )
    marque= Column(Integer,default="materiel simple")

class Gestion(Base):
    __tablename__ = "Historique des materiels"
    id = Column(Integer, primary_key=True, index=True)
    nom_professeur = Column(String(50), unique=True, index=True,nullable=False)
    nom_matiere=Column(String)
    nom_classe = Column(String)
    nom_materiel = Column(String)
    quantite_materiel = Column(Integer,default=0, nullable=False)
    nom_trimestre = Column(String)
    date=Column(DateTime, default=func.now())
