from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import schemas
import tasks
import services

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Route pour l'obtention d'un token d'accès
@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(services.get_db)
):
    # À noter que : username = email
    return await services.authenticate_user(db, form_data.username, form_data.password)

# Route pour ajouter un utilisateur
@app.post("/add/", response_model=schemas.User)
async def add_user(
    user: schemas.UserCreate,
    db: Session = Depends(services.get_db)
):
    return await services.add_user(db, user)

# Route pour récupérer tous les utilisateurs
@app.get("/users/", response_model=list[schemas.User])
async def read_users(
    db: Session = Depends(services.get_db)
):
    return await services.get_all_users(db)
