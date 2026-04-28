from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import  models
from database import get_db
router=APIRouter()

# ---ROUTES POUR ENREGISTRER LES DONNEES

@router.post("/enregistrement-trimestre")
def enregistreur_trimestre(trimestre: str,  debut: str, fin: str, db: Session = Depends(get_db)):
    if not trimestre:
        nouveau_debut = datetime.strptime(debut, "%Y-%m-%d")
        nouveau_fin = datetime.strptime(fin, "%Y-%m-%d")
        
        trimestre_enregistre = models.Trimestre(
            nom_trimestre=trimestre.lower(),
            date_debut=nouveau_debut,
            date_fin=nouveau_fin
        )
        db.add(trimestre_enregistre)
        db.commit()
        return {"status": "trimestre enregistrée !"}
    return{"Erreur":"Ce trimestre a déja été enregistré! Veuillez saisir un autre."}

@router.post("/enregistrement-classe")
def enregistreur_classe(classe: str, effectif:int, db: Session = Depends(get_db)):
    if not classe:
        classe_enregistre = models.Classe(
            nom_trimestre=classe.strip.lower(),
            nombre_effectif=effectif
        )
            
        db.add(classe_enregistre)
        db.commit()
        return {"status": "classe enregistré !"}
    return{"Erreur":"Cette Classe a déja été enregistré! Veuillez saisir un autre."}

@router.post("/enregistrement-Type Feuille")
def enregistreur_feuille(feuille: str, nombre:int, db: Session = Depends(get_db)):
    if not feuille:
        feuille_enregistre = models.Feuille(
            nom_feuille=feuille.strip.lower(),
            nombre_feuille=nombre
        )
        
        db.add(feuille_enregistre)
        db.commit()
        return {"status": "type de feuille enregistré !"}
    return{"Erreur":"Cette feuille a déja été enregistré. Veuillez saisir un autre!"}

@router.post("/enregistrement-Professeur")
def enregistreur_professeur(professeur: str, matiere:str, genre:str, db: Session = Depends(get_db)):
    if not professeur:
        professeur_enregistre = models.Professeur(
            genre_professeur=genre.lower(),
            nom_professeur=professeur.strip.lower(),
            nom_matiere=matiere
        )
        db.add(professeur_enregistre)
        db.commit()
        return {"status": "Professeur enregistré !"}
    return{"Erreur":"Ce Professeur a déja été enregistré. Veuillez saisir un autre!"}

# ---ROUTE POUR GESTION DES FEUILLES
@router.post("/enregistrement-feuille donné")
def enregistreur_feuille_donne(professeur: str, classe:str, feuille:str, nombre_feuille:int,
    db: Session = Depends(get_db)):
    gestion=db.querry(models.Gestion).all()
    trimestre_existe=db.query(models.Trimestre).filter(models.Trimestre.nom_trimestre).all()
    date_jour=datetime.now()
    matiere=db.query(models.Gestion).filter(
            models.Gestion.nom_matiere== professeur.strip.lower()).first()
    if gestion:
        for trimestre in trimestre_existe:
            trimestre_actuel=db.query(models.Trimestre).filter(
                models.Trimestre.nom_trimestre == trimestre.strip.lower(),
                models.Trimestre.date_debut <= date_jour,
                models.Trimestre.date_fin >= date_jour
            ).first()

            feuille_donne_enregistre = models.Professeur(
                nom_professeur=professeur.strip.lower(),
                nom_classe= classe.strip.lower(),
                nom_feuille=feuille.strip.lower(),
                nombre_feuille=nombre_feuille,
                nom_trimestre=trimestre_actuel,
                date=datetime.now,
                matiere=matiere
            )
            db.add(feuille_donne_enregistre)
            db.commit()
            return {
                "Professeur": professeur,
                "classe": classe,
                "feuille": feuille,
                "nombre de feuille": nombre_feuille
            }
    return {"Erreur":"Veuillez enregistrer d'abord les données de l'anneé scolaire"}
