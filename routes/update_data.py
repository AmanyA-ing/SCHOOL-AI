from fastapi import RouterAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models
from .. database import get_db

router=RouterAPI()

@router.patch("/modifier-gestion/{gestion_id}")
def modifier_gestion(gestion_id: int, donnes: dict, db: Session = Depends(get_db)):

    gestion = db.query(models.Gestion).filter(models.Gestion.id == gestion_id).first()
    
    if not gestion:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    for nom, valeur in donnes.items():
        if hasattr(gestion, nom):
            setattr(gestion, nom, valeur)
        else:
            continue 

    db.commit()
    db.refresh(gestion) 

    return {
        "message": "Modification effectuée avec succès",
        "donnees_mises_a_jour": gestion
    }

@router.patch("/modifier-trimestre/{trimestre_id}")
def modifer_trimestre(id_trimestre: int, donnes: dict , db: Session=Depends(get_db)):
    ligne_trimestre=db.query(models.Trimestre).filter(models.Trimestre.id==id_trimestre).first()
    if not ligne_trimestre:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    for nom, valeur in donnes.items():
        if hasattr(ligne_trimestre, nom):
            setattr(ligne_trimestre, nom, valeur)
        else:
            continue 

    db.commit()
    db.refresh(ligne_trimestre) 

    return {
        "message": "Modification effectuée avec succès",
        "donnees_mises_a_jour": ligne_trimestre
    }

@router.patch("/modifier-Classe/{classe_id}")
def modifer_classe(id_classe: int, donnes: dict , db: Session=Depends(get_db)):
    ligne_classe=db.query(models.Classe).filter(models.Classe.id==id_classe).first()
    if not ligne_classe:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    for nom, valeur in donnes.items():
        if hasattr(ligne_classe, nom):
            setattr(ligne_classe, nom, valeur)
        else:
            continue 

    db.commit()
    db.refresh(ligne_classe) 

    return {
        "Reussi": "Modification effectuée avec succès",
        "donnees_mises_a_jour": ligne_classe
    }

@router.patch("/modifier-Professeur/{professeur_id}")
def modifer_professeur(id_professeur: int, donnes: dict , db: Session=Depends(get_db)):
    ligne_professeur=db.query(models.Professeur).filter(models.Professeur.id==id_professeur).first()
    if not ligne_professeur:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    for nom, valeur in donnes.items():
        if hasattr(ligne_professeur, nom):
            setattr(ligne_professeur, nom, valeur)
        else:
            continue 

    db.commit()
    db.refresh(ligne_professeur) 

    return {
        "Reussi": "Modification effectuée avec succès",
        "donnees_mises_a_jour": ligne_professeur
    }
@router.patch("/modifier-Feuille/{feuille_id}")
def modifier_feuille(id_feuille: int, donnes: dict , db: Session=Depends(get_db)):
    ligne_feuille=db.query(models.Feuille).filter(models.Feuille.id==id_feuille).first()
    if not ligne_feuille:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    for nom, valeur in donnes.items():
        if hasattr(ligne_feuille, nom):
            setattr(ligne_feuille, nom, valeur)
        else:
            continue 

    db.commit()
    db.refresh(ligne_feuille) 

    return {
        "Reussi": "Modification effectuée avec succès",
        "donnees_mises_a_jour": ligne_feuille
    }
