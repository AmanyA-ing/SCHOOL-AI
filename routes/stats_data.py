from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from database import get_db
import models

router = APIRouter()

@router.get("/stats/professeur/{nom}")
def stats_detaillees_prof(nom: str, db: Session = Depends(get_db)):

    stats_par_type = db.query(
        models.Gestion.nom_materiel, 
        func.sum(models.Gestion.quantite_materiel).label("total_type"),
        func.avg(models.Gestion.quantite_materiel).label("moyenne_type")
    ).filter(
        models.Gestion.nom_professeur == nom
    ).group_by(
        models.Gestion.nom_materiel
    ).all()

    if not stats_par_type:
        raise HTTPException(status_code=404, detail=f"Aucune donnée pour le professeur {nom}")

    # .scalar() renvoie directement le chiffre au lieu d'une liste
    total_global = db.query(
        func.sum(models.Gestion.quantite_materiel)
    ).filter(models.Gestion.nom_professeur == nom).scalar() or 0

    # 3. Construction propre du JSON
    return {
        "professeur": nom,
        "bilan_global": total_global,
        "details": [
            {
                "outil": row.nom_materiel,
                "total": row.total_type,
                "moyenne": round(row.moyenne_type, 2)
            } for row in stats_par_type
        ]
    }

@router.get("/stats/top-consommateurs")
def stats_top_profs(limit: int = 5, db: Session = Depends(get_db)):
    top_profs = db.query(
        models.Gestion.nom_professeur,
        func.sum(models.Gestion.quantite_materiel).label("total")
    ).group_by(
        models.Gestion.nom_professeur
    ).order_by(
        func.sum(models.Gestion.quantite_materiel).desc()
    ).limit(limit).all()

    return [{"nom": r[0], "total": r[1]} for r in top_profs]