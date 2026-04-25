import app
@app.post("/enregistrement/trimestre")
def enregistreur_trimestre(trimestre: str,  debut: str, fin: str, db: Session = Depends(get_db)):

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

@app.post("/enregistrement/classe")
def enregistreur_classe(classe: str, effectif:int, db: Session = Depends(get_db)):

    classe_enregistre = models.Classe(
        nom_trimestre=classe.strip.lower(),
        nombre_effectif=effectif
    )
        
    db.add(classe_enregistre)
    db.commit()
    return {"status": "classe enregistré !"}

@app.post("/enregistrement/Type-Feuille")
def enregistreur_feuille(feuille: str, nombre:int, db: Session = Depends(get_db)):

    feuille_enregistre = models.Feuille(
        nom_feuille=feuille.strip.lower(),
        nombre_feuille=nombre
    )
        
    db.add(feuille_enregistre)
    db.commit()
    return {"status": "type de feuille enregistré !"}

@app.post("/enregistrement/Professeur")
def enregistreur_professeur(professeur: str, matiere:str, db: Session = Depends(get_db)):

    professeur_enregistre = models.Professeur(
        nom_professeur=professeur.strip.lower(),
        nom_matiere=matiere
    )
        
    db.add(professeur_enregistre)
    db.commit()
    return {"status": "Professeur enregistré !"}

# ---ROUTE POUR GESTIN DES FEUILLES
def enregistreur_feuille_donne(professeur: str, classe:str, feuille:str, nombre_feuille:int,
    db: Session = Depends(get_db)):
    trimestre_existe=db.query(models.Trimestre).filter(models.Trimestre.nom_trimestre).all()
    date_jour=datetime.now()
    if trimestre_existe:
        for trimestre in trimestre_existe:
            trimestre_actuel=db.query(models.Trimestre).filter(
        models.Trimestre.nom_trimestre == trimestre.strip.lower(),
        models.Trimestre.date_debut <= date_jour,
        models.Trimestre.date_fin >= date_jour
    ).first()
            
    return {"Alert:":"enregistrer les Trimestres/Semestres de l'anneé scolaire"}

    feuille_donne_enregistre = models.Professeur(
        nom_professeur=professeur.strip.lower(),
        nom_classe= classe.strip.lower(),
        nom_feuille=feuille.strip.lower(),
        nombre_feuille=nombre_feuille,
        nom_trimestre=trimestre_actuel,
        date=datetime.now
    )
        
    db.add(feuille_donne_enregistre)
    db.commit()
    return {
        "Professeur": professeur,
        "classe": classe,
        "feuille": feuille,
        "nombre de feuille": nombre_feuille
    }

    

