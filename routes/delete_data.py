from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
import models
from database import get_db, fichier_nom
import os
import shutil
router=APIRouter()

@router.delete("/supprimer-trimestre/{trimestre_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_trimestre(id_trimestre: int, db: Session=Depends(get_db)):
    ligne_trimestre=db.query(models.Trimestre).filter(models.Trimestre.id==id_trimestre).first()
    if not ligne_trimestre:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    db.query(models.Gestion).filter(
        models.Gestion.nom_professeur==ligne_trimestre.nom_processeur).delete()

    db.delete(ligne_trimestre)
    db.commit()

    return {
        "message": "trimestre supprimé avec succès!",
    }

@router.delete("/supprimer-Classe/{classe_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_classe(id_classe: int, db: Session=Depends(get_db)):
    ligne_classe=db.query(models.Classe).filter(models.Classe.id==id_classe).first()
    if not ligne_classe:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    db.query(models.Gestion).filter(
        models.Gestion.nom_classe==ligne_classe.nom_classe).delete()

    db.delete(ligne_classe)
    db.commit()

    return {
        "message": "classe supprimé avec succès!",
    }

@router.delete("/supprimer-Feuille/{feuille_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_feuille(id_feuille: int, db: Session=Depends(get_db)):
    ligne_feuille=db.query(models.Feuille).filter(models.Feuille.id==id_feuille).first()
    if not ligne_feuille:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    db.query(models.Gestion).filter(
        models.Gestion.nom_classe==ligne_feuille.nom_feuille).delete()

    db.delete(ligne_feuille)
    db.commit()

    return {
        "Réussi": "feuille supprimé avec succès!",
    }

@router.delete("/supprimer-Professeur/{professeur_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_professeur(id_professeur: int, db: Session=Depends(get_db)):
    ligne_professeur=db.query(models.Professeur).filter(
        models.Professeur.id==id_professeur).first()
    if not ligne_professeur:
        raise HTTPException(status_code=404, detail="Enregistrement introuvable")
    db.query(models.Gestion).filter(
        models.Gestion.nom_classe== ligne_professeur.nom_professeur).delete()

    db.delete(ligne_professeur)
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
        
        shutil.copy2("./bosco.db", nom_archive)

        db.query(models.Gestion).delete()
        db.query(models.Feuille).delete()
        db.query(models.Classe).delete()
        db.query(models.Trimestre).delete()
        db.query(models.Professeur).delete()
        
        db.commit()
        
        return {
            "message": "Réinitialisation réussie",
            "archive_crée": nom_archive
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
    