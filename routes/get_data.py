from fastapi import RouterAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models
from .. database import get_db
router=APIRouter()

@router.get("/voir-trimestre")
def voir_trimestre(db: Session = Depends(get_db)):
   
    trimestre = db.query(models.Trimestre).all()
    if trimestre:
        return {
            "trimestre": trimestre

        }
    return { "Aucun trimestre/semestre n'a été enregistré."}


@router.get("/voir-classe")
def voir_classe(db: Session = Depends(get_db)):
   
    classe= db.query(models.Classe).all()
    if classe: 
        return {
            "Classe": classe
        } 
    return { "Aucune classe n'a été enregistrée."}

@router.get("/voir-feuille")
def voir_feuille(db: Session = Depends(get_db)):
    
    feuille = db.query(models.Feuille).filter(models.Feuille.nom_feuille.strip.lower()).first()
    
    if feuille:
        return {
            "Type de Feuille":feuille
        }
    return { "Aucune feuille n'a été enregistrée."}

@router.get("/voir-Professeur")
def voir_feuille(db: Session = Depends(get_db)):
    professeur_total=db.query(models.Professeur).all()
    professeur = db.query(models.Professeur).filter(models.Professeur.nom_professeur).first()
    matiere = db.query(models.Professeur).filter(models.Professeur.nom_matiere).first()
    genre= db.query(models.Professeur).filter(models.Professeur.nom_matiere).first()
    
    if professeur_total:
        return {
            "Professeur ":professeur,
            "Matiere":matiere,
            "Genre":genre
            }
    return { "Aucun Professeur n'a été enregistré."}
    
@router.get("/verifier feuille")
def voir_feuille_donné(db: Session = Depends(get_db))
    gestion=db.querry(models.Gestion).all()

    trimestre_enregistre=db.query(models.Trimestre).filter(models.Trimestre.nom_trimestre).all()

    date_enregistrement=db.query(models.Gestion).filter(
                models.Gestion.nom_trimestre == trimestre.strip.lower(),
                models.Trimestre.date
            ).first()

    trimestre=db.query(models.Trimestre).filter(
                models.Trimestre.nom_trimestre == trimestre.strip.lower(),
                models.Trimestre.date_debut <= date_enregistrement,
                models.Trimestre.date_fin >= date_enregistrement).first()

    feuille_donne=db.querry(models.gestion).all()

    if gestion:
        for trimestre in trimestre_enregistre:
       
            return{
                "trimestre:":"{trimestre_enregistré}",
                "feuille donne":feuille_donne
            }
    return { "Aucune feuille n'a été donnée à un Professeur."}

