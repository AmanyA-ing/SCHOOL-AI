from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter()

@router.get("/suggestions/professeurs")
def rechercher_professeur(recherche: str, db: Session = Depends(get_db)):
    try:
        professeur_suggere = db.query(models.Professeur).filter(
            models.Professeur.nom_professeur.ilike(f"%{recherche.strip()}%")
        ).limit(10).all() 
    
        return [{"Professeur": p.nom_professeur} for p in professeur_suggere]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/suggestions/materiels")
def suggerer_materiel(db: Session = Depends(get_db)):
    try:
        materiel_enregistre = db.query(models.Materiel.nom_materiel).all()
        return [materiel[0] for materiel in materiel_enregistre]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/suggestions/trimestres")
def suggerer_Trimestre(db: Session = Depends(get_db)):
    try:
        trimestre_enregistre = db.query(models.Trimestre.nom_trimestre).all()
        return [trimestre[0] for trimestre in trimestre_enregistre]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/classe/info/{nom}")
def suggerer_classe_materiel(nom: str, db: Session = Depends(get_db)):
    classe = db.query(models.Classe).filter(models.Classe.nom_classe == nom).first()
    if classe:
        return {
            "Classe": classe.nom_classe, 
            "effectif": classe.nombre_effectif
        }
    return {}