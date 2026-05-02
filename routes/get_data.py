from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from datetime import datetime, timedelta
import models
from database import get_db
router=APIRouter()

@router.get("/voir-trimestre")
def voir_trimestre(db: Session = Depends(get_db)):
    trimestres = db.query(models.Trimestre).all()
    
    if not trimestres:
        return {"message":"Aucun trimestre enregistré"}

    return trimestres

@router.get("/voir-classe")
def voir_classe(db: Session = Depends(get_db)):
   
    classe= db.query(models.Classe).all()
    if not classe:  
        return { "message":"Aucune classe n'a été enregistrée."}
    return classe

@router.get("/voir-materiel")
def voir_materiel(db: Session = Depends(get_db)):
    
    materiel = db.query(models.Materiel).all()
    return materiel if materiel else { "message":"Aucun materiel n'a été enregistré."}

@router.get("/voir-Professeur")
def voir_professeur(db: Session = Depends(get_db)):
    professeur_total=db.query(models.Professeur).all()
    return professeur_total if professeur_total else {"message":"Aucun professeur n'a été enregistré"}
    
@router.get("/voir-historique")
def voir_historique_mensuel(nom_prof: str = None, db: Session = Depends(get_db)):

    il_y_a_30_jours = datetime.now() - timedelta(days=30)
    
    query = db.query(models.Gestion).filter(models.Gestion.date >= il_y_a_30_jours)

    if nom_prof:

        query = query.filter(models.Gestion.nom_professeur.ilike(f"%{nom_prof.strip()}%"))


    enregistrements = query.order_by(desc(models.Gestion.date)).limit(40).all()
    liste_finale = [
        {
            "professeur": ligne.nom_professeur,
            "classe": ligne.nom_classe,
            "materiel": ligne.nom_materiel,
            "quantite": ligne.quantite_materiel,
            "date": ligne.date.strftime("%d/%m/%Y à %H:%M") # Format plus complet
        } 
        for ligne in enregistrements
    ]

    return {"historique": liste_finale}