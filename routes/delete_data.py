from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
import models
from database import get_db, fichier_nom
import os
import shutil
router=APIRouter()

@router.delete("/supprimer-trimestre/{id_trimestre}") 
def supprimer_trimestre(id_trimestre: int, db: Session = Depends(get_db)):

    trimestre = db.query(models.Trimestre).filter(models.Trimestre.id == id_trimestre).first()
    
    if not trimestre:
        raise HTTPException(status_code=404, detail="Trimestre introuvable")

    db.query(models.Gestion).filter(
        models.Gestion.nom_trimestre == trimestre.nom_trimestre
    ).delete()

    db.delete(trimestre)
    db.commit()

    return {"message": f"Le trimestre {trimestre.nom_trimestre} et ses données ont été supprimés."}

@router.delete("/supprimer-Classe/{classe_id}")
def supprimer_classe(id_classe: int, db: Session=Depends(get_db)):

    classe=db.query(models.Classe).filter(models.Classe.id==id_classe).first()
    if not classe:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    
    db.query(models.Gestion).filter(
        models.Gestion.nom_classe==classe.nom_classe
        ).delete()

    db.delete(classe)
    db.commit()

    return { 
        "message": f"La classe {classe.nom_classe} et ses données ont été supprimés."}

@router.delete("/supprimer-Materiel/{materiel_id}")
def supprimer_materiel(id_materiel: int, db: Session=Depends(get_db)):
    materiel=db.query(models.Materiel).filter(models.Materiel.id==id_materiel).first()
    if not materiel:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")

    db.query(models.Gestion).filter(
        models.Gestion.nom_materiel==materiel.nom_materiel).delete()

    db.delete(materiel)
    db.commit()

    return {
        "Réussi":  f"Le materiel {matieriel.nom_materiel} et ses données ont été supprimés.",
    }

@router.delete("/supprimer-Professeur/{professeur_id}")
def supprimer_professeur(id_professeur: int, db: Session=Depends(get_db)):
    professeur=db.query(models.Professeur).filter(
        models.Professeur.id==id_professeur).first()
    if not professeur:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    db.query(models.Gestion).filter(
        models.Gestion.nom_professeur== professeur.nom_professeur).delete()

    db.delete(professeur)
    db.commit()

    return {
        "Validé": "Professeur supprimé avec succès!",
    }

@router.delete("/supprimer-Gestion/{gestion_id}")
def supprimer_gestion( db: Session=Depends(get_db)):
    ligne_gestion=db.query(models.Gestion).all()
    if not ligne_gestion:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    
    try:
        db.querry(models.Gestion).delete()
        db.commit()
        return {
            "Reussi": "nettoyage effectué.",
        }
    except Exception:
        db.rollback()
        return{"Erreur":"Veuillez réssayer plus tard"}

@router.delete("/supprimer-tout")
def supprimer_tout(db: Session = Depends(get_db)):
    try:
        if not os.path.exists("./archives_db"):
            os.makedirs("./archives_db_")
            
        jour_renitialiser= datetime.now().strftime("%Y")
        nom_archive = f"./archives_db/{fichier_nom}-{jour_renitialiser}".db
        
        shutil.copy2(f"./bosco{fichier_nom}.db", nom_archive)

        db.query(models.Gestion).delete()
        db.query(models.Trimestre).delete()        
        db.commit()
        
        return {
            "message": "Réinitialisation réussie",
            "archive_crée": nom_archive
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
    