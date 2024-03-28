# --- Importation des modules
# -- Fast API
from fastapi import FastAPI, Depends
# OAuth2PasswordBearer est utilisé pour la gestion de l'authentification, OAuth2PasswordRequestForm est utilisé pour la gestion de la requête d'authentification
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# CORS est utilisé pour la gestion des requêtes CORS
from fastapi.middleware.cors import CORSMiddleware
# --- SQLAlchemy
from sqlalchemy.orm import Session
# datetime est utilisé pour la gestion des dates
from datetime import datetime
# typing.Annotated est utilisé pour la gestion des annotations
from typing import Annotated
import schemas, services

# --- Catégories des endpoints (voir documentations Swagger/redocs)
tags_metadata = [
     {
        "name": "Server",
        "description": "Monitor the server state",
    },
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Deck",
        "description": "Operations with decks.",
    },
    {
        "name": "Card",
        "description": "Operations with cards.",
    },
    {
        "name": "Train",
        "description": "Operations with training.",
    },
]

# --- FastAPI app
app = FastAPI(
    title="NotaBene API",
    description="This is the API documentation for the NotaBene project ✨📚",
)

# Migration de la base de données
services.create_database()

# Instance de la base de données
services.get_db()

# --- Configuration CORS
# il est possible de passer un tableau avec les origines autorisées, les méthodes autorisées, les en-têtes autorisés, etc.
# ici, on autorise toutes les origines, les méthodes, les en-têtes, etc car on est en développement, en production, il faudra restreindre ces valeurs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Créer une instance de OAuth2PasswordBearer avec l'URL personnalisée
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Routes
# --- Server
@app.get("/", tags=["Server"])
async def root():
    """
    Cette route permet de vérifier si le serveur est en ligne
    """
    return {"message": "NotaBene API is online, welcome to the API documentation at /docs or /redocs"}

@app.get("/unixTimes", tags=["Server"])
async def read_item():
    """
    Cette route permet de récupérer le temps UNIX
    """
    unix_timestamp = datetime.now().timestamp()
    return {"unixTime": unix_timestamp}

# --- Users
# On ne peut pas changer le nom de la route, c'est une route prédéfinie par FastAPI
@app.post("/token", response_model=schemas.Token, tags=["Users"])
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(services.get_db)
)-> schemas.Token:
    """
    Cette route permet de se connecter et de récupérer un token d'accès, à noter qu'ici : username = email
    @param form_data: OAuth2PasswordRequestForm
    @param db: Session
    @return schemas.Token
    """
    return await services.authenticate_user(db, form_data.username, form_data.password)

@app.get("/users/", response_model=list[schemas.User], tags=["Users"])
async def read_users(
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> list[schemas.User]:
    """
    Cette route permet de récupérer tous les utilisateurs
    @param db: Session
    @return list[schemas.User]
    """
    return await services.get_all_users(db)

@app.post("/users/", response_model=schemas.User, tags=["Users"])
async def add_user(
    user: schemas.UserCreate,
    db: Session = Depends(services.get_db)
)-> schemas.User:
    """
    Cette route permet d'ajouter un utilisateur
    @param user: schemas.UserCreate
    @param db: Session
    @return schemas.User
    """
    return await services.add_user(db, user)

@app.get("/users/me/", response_model=schemas.User, tags=["Users"])
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(services.get_current_user)]
):
    return current_user

@app.post("/users/follow/", response_model=schemas.User, tags=["Users"])
async def follow(
    user_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> schemas.User:
    """
    Cette fonction permet de suivre un utilisateur
    @param user_id: int
    @param current_user: schemas.User
    @param db: Session
    @return schemas.User
    """
    return await services.follow(db, user_id, current_user)

@app.patch("/users/active-deck", response_model=schemas.User, tags=["Users"])
async def set_active_deck(
    deck_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> schemas.User:
    """
    Cette route permet de définir un deck actif pour un utilisateur
    @param user_id: int
    @param deck_id: int
    @param current_user: schemas.User
    @param db: Session
    @return schemas.User
    """
    return await services.set_active_deck(db, deck_id, current_user)

# routes qui récupère le deck actif 
@app.get("/users/active-deck", response_model=schemas.Deck, tags=["Users"])
async def get_active_deck(
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> schemas.Deck:
    """
    Cette route permet de récupérer le deck actif d'un utilisateur
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.get_active_deck(db, current_user)

# --- Deck
@app.get("/decks/", response_model=list[schemas.Deck], tags=["Deck"])
async def read_decks(
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> list[schemas.Deck]:
    """
    Cette route permet de récupérer tous les decks de l'utilisateur connecté
    @param current_user: schemas.User
    @param db: Session
    @return list[schemas.Deck]
    """
    return await services.get_decks(db, current_user)

@app.put("/decks/{deck_id}", response_model=schemas.Deck, tags=["Deck"])
async def update_deck(
    deck_id: int,
    deck: schemas.DeckBase,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db),
)-> schemas.Deck:
    """
    Cette route permet de modifier un deck
    @param deck_id: int
    @param deck: schemas.DeckBase
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.update_deck(db, deck_id, deck, current_user)

@app.get("/decks/{deck_id}", response_model=schemas.Deck, tags=["Deck"])
async def read_deck(
    deck_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db),
)-> schemas.Deck:
    """
    Cette route permet de récupérer un deck spécifique
    @param deck_id: int
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.get_deck(db, deck_id, current_user)

@app.post("/decks/", response_model=schemas.Deck, tags=["Deck"])
async def add_deck(
    deck: schemas.DeckBase,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> schemas.Deck:
    """
    Cette route permet d'ajouter un deck
    @param deck: schemas.DeckBase
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.add_deck(db, deck, current_user)

# delete deck 
@app.delete("/decks/{deck_id}", response_model=schemas.Deck, tags=["Deck"])
async def delete_deck(
    deck_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> schemas.Deck:
    """
    Cette route permet de supprimer un deck
    @param deck_id: int
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.delete_deck(db, deck_id, current_user)
@app.patch("/decks/visibility/{deck_id}", response_model=schemas.Deck, tags=["Deck"])
async def update_deck(
    deck_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    visibility: schemas.Visibility,
    db: Session = Depends(services.get_db),
)-> schemas.Deck:
    """
    Cette route permet de modifier la visibilité d'un deck
    @param deck_id: int
    @param visibility: str
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.update_deck_visibility(db, deck_id, visibility, current_user)


# Route qui permet de copier le deck d'un utilisateur et l'ajouter dans nos decks
@app.post("/decks/copy/{deck_id}", response_model=schemas.Deck, tags=["Deck"])
async def copy_deck(
    deck_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db),
)-> schemas.Deck:
    """
    Cette route permet de copier un deck d'un utilisateur
    @param deck_id: int
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Deck
    """
    return await services.copy_deck(db, deck_id, current_user)




# --- Cards
@app.post("/cards/", response_model=schemas.Card, tags=["Card"])
async def add_card(
    card: schemas.CardBase,
    deck_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db)
)-> schemas.Card:
    """
    Cette route permet d'ajouter une carte à un deck
    @param card: schemas.CardBase
    @param deck_id: int
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Card
    """
    return await services.add_card(db, card, deck_id)

@app.patch("/cards/{card_id}", response_model=schemas.Card, tags=["Card"])
async def update_card(
    card_id: int,
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    state: schemas.State,
    db: Session = Depends(services.get_db),
)-> schemas.Card:
    """
    Cette route permet de modifier le statut d'une carte
    @param card_id: int
    @param card: schemas.CardBase
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Card
    """
    return await services.update_card(db, card_id, state, current_user)

# --- Train
@app.get("/train/", tags=["Train"])
async def play_deck(
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db),
) -> schemas.Card:
    """
    Cette route permet de jouer avec un deck
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Card
    """
    return await services.play_deck(db, current_user)


@app.get("/train/random", response_model=schemas.Card, tags=["Train"])
async def read_random_card(
    current_user: Annotated[schemas.User, Depends(services.get_current_user)],
    db: Session = Depends(services.get_db),
)-> schemas.Card:
    """
    Cette route permet de récupérer une carte aléatoire d'un deck
    @param current_user: schemas.User
    @param db: Session
    @return schemas.Card
    """
    return await services.get_random_card(db, current_user)
