from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import  models
from database import get_db

router=APIRouter()

# ---ROUTES POUR ENREGISTRER LES DONNEES

@router.post("/enregistrement-trimestre")
def enregistreur_trimestre(trimestre: str,  debut: str, fin: str, db: Session = Depends(get_db)):
    trim_propre=trimestre.upper().strip()
    existe=db.query(models.Trimestre).filter(models.Trimestre.nom_trimestre == trim_propre).first()
    
    if not trim_propre:
        raise HTTPException(status_code=400, detail="Le nom du trimestre est obligatoire.")
    if  existe:
        raise HTTPException(status_code=400, detail="Ce trimestre est déja enregisré!")
    
    nouveau_debut = datetime.strptime(debut, "%Y-%m-%d")
    nouveau_fin = datetime.strptime(fin, "%Y-%m-%d")
        
    trimestre_enregistre = models.Trimestre(
        nom_trimestre=trim_propre,
        date_debut=nouveau_debut,
        date_fin=nouveau_fin
    )
    try:
        db.add(trimestre_enregistre)
        db.commit()
        return {"status": "trimestre enregistrée !"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erreur lors de l'enregistrement de {trim_propre}.")

@router.post("/enregistrement-classe")
def enregistreur_classe(classe: str, effectif:int, db: Session = Depends(get_db)):
    classe_saisi=classe.strip().replace(" ","").upper()
    classe_existe=db.query(models.Classe).filter(models.Classe.nom_classe == classe_saisi).first()
    if not classe_saisi:
        raise HTTPException(status_code=400, detail="Le nom de la classe est obligatoire.")
   
    if classe_existe:
        raise HTTPException(status_code=400, detail="Cette classe a déja été enregistré! Veuillez saisir un autre.")
    
    classe_enregistre = models.Classe(
            nom_classe=classe_saisi,
            nombre_effectif=effectif
        )
            
    db.add(classe_enregistre)
    db.commit()
    return {"status": "classe enregistré !"}

@router.post("/enregistrement-Type materiel")
def enregistreur_materiel(materiel: str, nombre:int, db: Session = Depends(get_db)):
    materiel_saisi=materiel.strip().upper()
    materiel_existe=db.query(models.Materiel).filter(models.Materiel.nom_materiel == materiel_saisi).first()
    
    if not materiel_saisi:
        raise HTTPException(status_code=400, detail="Le nom du matériel est obligatoire.")
    if materiel_existe:
        raise HTTPException(status_code=400, detail="Ce matériel a déja été enregistré! Veuillez saisir un autre.")

    materiel_enregistre = models.Materiel(
            nom_materiel=materiel_saisi,
            quantite_materiel=nombre
        )
        
    db.add(materiel_enregistre)
    db.commit()
    return {"status": "type de materiel enregistré !"}

@router.post("/enregistrement-Professeur")
def enregistreur_professeur(professeur: str, matiere:str, genre:str, db: Session = Depends(get_db)):
    
    prof_saisi = professeur.strip().upper()
    mat_saisi = matiere.strip().capitalize()
    if not prof_saisi:
        raise HTTPException(status_code=400, detail="Le nom du professeur est obligatoire")
    if not mat_saisi:
        raise HTTPException(status_code=400, detail="La matière est obligatoire")
    if not genre:
        raise HTTPException(status_code=400, detail="Le genre est obligatoire")
    
    prof_existe = db.query(models.Professeur).filter(models.Professeur.nom_professeur == prof_saisi).first()    
    matiere_existe= db.query(models.Professeur).filter(models.Professeur.nom_matiere == mat_saisi).first()
    if prof_existe:
        raise HTTPException(status_code=400, detail="Ce professeur existe déjà")
    if matiere_existe:
        raise HTTPException(status_code=400, detail="Cette matière est déjà enseignée par un autre professeur")
    
    nouveau_prof = models.Professeur(
        genre_professeur=genre.upper(),
        nom_professeur=prof_saisi,
        nom_matiere=mat_saisi
    )
    db.add(nouveau_prof)
    db.commit()
    return {"message": "Professeur enregistré avec succès"}

# ---ROUTE POUR GESTION DES materielS
@router.post("/gestion-materiel")
def enregistreur_materiel_donne(professeur: str, classe:str, materiel:str, quantite_materiel:int,
    db: Session = Depends(get_db)):
    prof_saisi=professeur.strip().upper() if professeur else ""
    classe_saisi=classe.strip().upper().replace(" ","") if classe else ""
    materiel_saisi=materiel.strip().capitalize() if materiel else ""
    if not prof_saisi or not classe_saisi or not materiel_saisi or not quantite_materiel :
        raise HTTPException(status_code=400, detail="Entrez une donnée dans tous les champs.")
    if quantite_materiel <= 0:
        raise HTTPException(status_code=400, detail="La quantité de matériel doit être un nombre positif.") 
    
    date_actuel=datetime.now()
    prof_correspondant=db.query(models.Professeur).filter(
        models.Professeur.nom_professeur==prof_saisi).first()
    matiere=db.query(models.Matiere).filter(models.Matiere.nom_matiere== prof_correspondant).first()
    trimestre_actuel = db.query(models.Trimestre).filter(
        models.Trimestre.date_debut <= date_actuel,
        models.Trimestre.date_fin >= date_actuel
    ).first()

    materiel_donne_enregistre = models.Gestion(
                nom_trimestre=trimestre_actuel.nom_trimestre,
                nom_professeur=prof_saisi,
                nom_classe= classe_saisi,
                nom_materiel=materiel_saisi,
                quantite_materiel=quantite_materiel,
                date=date_actuel,
                matiere=matiere
                )
    
    db.add(materiel_donne_enregistre)
    db.commit()
    return {
                "Professeur": professeur,
                "classe": classe,
                "materiel": materiel,
                "nombre de materiel": quantite_materiel
            }
