from fastapi import FastAPI
from database import init_db
from routes import update_data, get_data, delete_data, recorder_data

app = FastAPI(title="BOSCO AI")
init_db()

app.include_router(recorder_data.router, prefix="/api",tags=["Enregistreur de donnes"])
app.include_router(get.router, prefix="/api",tags=["Affichage"])
app.include_router(update_data.router, prefix="/api",tags=["Modifier donnés"])
app.include_router(delete.router, prefix="/api",tags=["Supprimés donnés"])

@app.get("/")
def home():
    return {"message":"Serveur School  AI opértionnel !"}


