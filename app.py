from fastapi import FastAPI
from database import  Base, engine
from routes import update_data, get_data, delete_data, record_data, suggestion_data, stats_data
import models
app = FastAPI(title="SCHOOL AI") 
models.Base.metadata.create_all(bind=engine)

# Inclusion des routes
app.include_router(record_data.router, prefix="/api", tags=["Enregistrement"])
app.include_router(get_data.router, prefix="/api", tags=["Affichage"])
app.include_router(update_data.router, prefix="/api", tags=["Modification"])
app.include_router(delete_data.router, prefix="/api", tags=["Suppression"])
app.include_router(suggestion_data.router, prefix="/api", tags=["Suggestions"])
app.include_router(stats_data.router, prefix="/api", tags=["Statistique"])


@app.get("/")
def home():
    return {"Bienvenue": "Serveur School AI opérationnel !"}