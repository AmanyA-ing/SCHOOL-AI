from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from datetime import datetime, timedelta
from database import get_db
from models import Gestion

router = APIRouter()

@router.get("/stats/recherche")
def voir_satistiques(professeur: str, db: Session = Depends(get_db)):
    
    prof_enregistre = db.query(Gestion).filter(Gestion.nom_professeur == professeur).all()
    
    if not prof_enregistre:
        return {"message": "Professeur non trouvé ou aucune donnée"}

    stats_detailles = {}
    grand_total = 0

    for prof in prof_enregistre:
        type_feuille = prof_enregistre.type_feuille
        nb_feuille = prof_enregistre.nombre_feuille
        
        stats_detailles[type_feuille] = stats_detailles.get(type_feuille, 0) + nb_feuille
        grand_total += nb_feuille

    return {
        "professeur": professeur,
        "details": stats_detailles, # {"Interro": 50, "Devoir": 100}
        "grand_total": grand_total    
    }

@router.get("/stats/hebdo")
def stats_semaine_en_cours(db: Session = Depends(get_db)):
    aujourdhui = datetime.now()
    lundi_dernier = aujourdhui - timedelta(days=aujourdhui.weekday())
    lundi_minuit = lundi_dernier.replace(hour=0, minute=0, second=0, microsecond=0)

    resultat = db.query(
        Gestion.nom_professeur, 
        func.sum(Gestion.nombre_feuille).label("total")
    ).filter(Gestion.date >= lundi_minuit).group_by(Gestion.nom_professeur).all()

    return [{"professeur": r[0], "total": r[1]} for r in resultat]