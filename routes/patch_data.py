from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import models
from database import get_db
router=APIRouter()


@router.patch("/modifier-trimestre/{id_trimestre}")
def modifier_trimestre(id_trimestre: int, donnes_trim: dict, db: Session = Depends(get_db)):

    ligne_trimestre = db.query(models.Trimestre).filter(models.Trimestre.id == id_trimestre).first()
    
    if not ligne_trimestre:
        raise HTTPException(status_code=404, detail="Trimestre introuvable")

    champs_interdits = ["id","date"]

    for nom, valeur in donnes_trim.items():
        if hasattr(ligne_trimestre, nom) and nom not in champs_interdits and valeur is not None:
            setattr(ligne_trimestre, nom, valeur)

    db.commit()
    db.refresh(ligne_trimestre) 

    return {
        "message": "Modification réussie",
        "nouveau_trimestre": {
            "nom": ligne_trimestre.nom_trimestre,
            "debut": ligne_trimestre.date_debut,
            "fin": ligne_trimestre.date_fin
        }
    }

@router.patch("/modifier-Classe/{id_classe}")
def modifer_classe(id_classe: int, donnes: dict , db: Session=Depends(get_db)):

    ligne_classe = db.query(models.Classe).filter(models.Classe.id == id_classe).first()
    
    if not ligne_classe:
        raise HTTPException(status_code=404, detail="Classe introuvable")

    champs_interdits = ["id", "date"]

    for nom, valeur in donnes.items():
        if hasattr(ligne_classe, nom) and nom not in champs_interdits and valeur is not None:
            setattr(ligne_classe, nom, valeur)

    db.commit()
    db.refresh(ligne_classe)

    return {
        "status": "success",
        "message": "Classe mise à jour",
        "donnees": ligne_classe
    }

@router.patch("/modifier-professeur/{id_professeur}")
def modifier_professeur(id_professeur: int, donnes: dict, db: Session = Depends(get_db)):
    ligne_professeur = db.query(models.Professeur).filter(models.Professeur.id == id_professeur).first()
    
    if not ligne_professeur:
        raise HTTPException(status_code=404, detail="Professeur introuvable")

    champs_interdits = ["id","date"]

    for nom, valeur in donnes.items():
        if hasattr(ligne_professeur, nom) and nom not in champs_interdits and valeur is not None:
            setattr(ligne_professeur, nom, valeur)

    db.commit()
    db.refresh(ligne_professeur)

    return {
        "status": "success",
        "message": "Profil professeur mis à jour",
        "donnees": ligne_professeur
    }

@router.patch("/modifier-materiel/{id_materiel}")
def modifier_materiel(id_materiel: int, donnes: dict, db: Session = Depends(get_db)):
    # Attention au nom du modèle : models.Materiel (avec une majuscule souvent)
    ligne_materiel = db.query(models.Materiel).filter(models.Materiel.id == id_materiel).first()
    
    if not ligne_materiel:
        raise HTTPException(status_code=404, detail="Matériel introuvable")

    champs_interdits = ["id", "date"]

    for nom, valeur in donnes.items():
        if hasattr(ligne_materiel, nom) and nom not in champs_interdits and valeur is not None:
            setattr(ligne_materiel, nom, valeur)

    db.commit()
    db.refresh(ligne_materiel)

    return {
        "status": "success",
        "message": "Stock matériel mis à jour",
        "donnees": ligne_materiel
    }

@router.patch("/modifier-gestion/{id_gestion}")
def modifier_gestion(id_gestion: int, donnes: dict, db: Session = Depends(get_db)):
    ligne_gestion = db.query(models.Gestion).filter(models.Gestion.id == id_gestion).first()
    
    if not ligne_gestion:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    champs_interdits = ["id", "date"]

    for nom, valeur in donnes.items():
        if hasattr(ligne_gestion, nom) and nom not in champs_interdits and valeur is not None:
            setattr(ligne_gestion, nom, valeur)

    db.commit()
    db.refresh(ligne_gestion) 

    return {
        "status": "success",
        "message": "Enregistrement de gestion mis à jour",
        "donnees": ligne_gestion
    }
