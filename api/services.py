# --- Importation des modules
# sqlalchemy.orm est utilisé pour la session de la base de données, cela permet d'accéder à la base de données, de la lire et de l'écrire, etc.
from sqlalchemy.orm import Session
# fastapi.HTTPException est utilisé pour lever des exceptions HTTP
from fastapi import HTTPException, status, Depends
# OAuth2PasswordBearer est utilisé pour la gestion de l'authentification
from fastapi.security import OAuth2PasswordBearer
# typing.Annotated est utilisé pour les annotations
from typing import Annotated
# jose.JWTError est utilisé pour gérer les erreurs liées au JWT, jose.jwt est utilisé pour la gestion des JWT
from jose import JWTError
import models, schemas, tasks, database, random

# --- Configuration de l'authentification
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Fonctions de services
def create_database():
    """
    Cette fonction permet de créer la base de données
    @return None
    """
    return database.Base.metadata.create_all(bind=database.engine)

def get_db() -> Session:
    """
    Cette fonction permet de récupérer la session de la base de données
    @return Session
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Users
async def get_all_users(db: Session) -> list:
    """
    Cette fonction permet de récupérer tous les utilisateurs
    @param db: Session
    @return list
    """
    return db.query(models.User).all()

async def add_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Cette fonction permet d'ajouter un utilisateur
    @param db: Session
    @param user: schemas.UserCreate
    @return models.User
    """
    hashed_password = tasks.get_password_hash(user.password)
    db_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=hashed_password,
        rgpd=user.rgpd,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def authenticate_user(db: Session, email: str, password: str):
    """
    Cette fonction permet d'authentifier un utilisateur
    @param db: Session
    @param email: str
    @param password: str
    @return dict
    """
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not tasks.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = tasks.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

async def follow(db: Session, user_id: int, current_user: models.User) -> models.User:
    """
    Cette fonction permet de suivre un utilisateur
    @param db: Session
    @param user_id: int
    @param current_user: models.User
    @return models.User
    """
    friend = db.query(models.User).filter(models.User.id == user_id).first()
    if friend is None:
        raise HTTPException(status_code=404, detail="User not found")
    current_user.following.append(friend)
    db.commit()
    db.refresh(current_user)
    return current_user

async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> models.User:
    """
    Cette fonction permet de récupérer l'utilisateur actuel
    @param db: Session
    @param token: str
    @return models.User
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = tasks.jwt.decode(token, tasks.SECRET_KEY, algorithms=[tasks.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

async def set_active_deck(db: Session, deck_id: int, user: models.User) -> models.User:
    """
    Cette fonction permet de définir le deck actif d'un utilisateur
    @param db: Session
    @param deck_id: int
    @param user: models.User
    @return models.User
    """
    user.active_deck_id = deck_id
    db.commit()
    db.refresh(user)
    return user

# --- Decks
async def add_deck(db: Session, deck: schemas.DeckCreate, user: models.User) -> models.Deck:
    """
    Cette fonction permet d'ajouter un deck
    @param db: Session
    @param deck: schemas.DeckCreate
    @param user: models.User
    @return models.Deck
    """
    db_deck = models.Deck(
        name=deck.name,
        visibility=deck.visibility,
        color=deck.color,
        owner_id=user.id
    )
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)

    # ajoute le deck à la liste des decks de l'utilisateur
    user.decks.append(db_deck)
    db.commit()
    db.refresh(user)

    # ajoute la progression du deck à la liste des progressions de l'utilisateur 
    db_progress = models.DeckProgress(
        user_id=user.id,
        deck_id=db_deck.id,
        progress=0
    )
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)

    user.deck_progress.append(db_progress)
    db.commit()
    db.refresh(user)

    if len(user.decks) == 1:
        user.active_deck_id = db_deck.id
        db.commit()
        db.refresh(user)

    return db_deck

async def get_decks(db: Session, user: models.User) -> list:
    """
    Cette fonction permet de récupérer tous les decks d'un utilisateur
    @param db: Session
    @param user: models.User
    @return list
    """
    return user.decks

async def get_deck(db: Session, deck_id: int, user: models.User) -> models.Deck:
    """
    Cette fonction permet de récupérer un deck spécifique 
    @param db: Session
    @param deck_id: int
    @param user: models.User
    @return models.Deck
    """
    # s'il n'est pas dans deck_progress de l'utilisateur
    # if deck_id not in [deck_progress.deck_id for deck_progress in user.deck_progress]:
    #     raise HTTPException(status_code=404, detail="Deck not found")

    # s'il n'est pas dans les decks de l'utilisateur
    if deck_id not in [deck.id for deck in user.decks]:
        raise HTTPException(status_code=404, detail="Deck not found")

    return db.query(models.Deck).filter(models.Deck.id == deck_id).first()

# choix de la visibilité du deck
async def update_deck_visibility(db: Session, deck_id: int, visibility: str, user: models.User) -> models.Deck:
    """
    Cette fonction permet de mettre à jour la visibilité d'un deck
    @param db: Session
    @param deck_id: int
    @param visibility: str
    @param user: models.User
    @return models.Deck
    """
    deck = db.query(models.Deck).filter(models.Deck.id == deck_id).first()
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    
    # Tu dois être le propriétaire du deck pour changer la visibilité
    if deck.owner_id != user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of the deck")
    deck.visibility = visibility
    db.commit()
    db.refresh(deck)
    return deck


async def copy_deck(db: Session, deck_id: int, user: models.User) -> models.Deck:
    """
    Cette fonction permet de copier le deck d'un utilisateur et l'ajouter dans nos decks
    @param db: Session
    @param deck_id: int
    @param user: models.User
    @return models.Deck
    """
    deck = db.query(models.Deck).filter(models.Deck.id == deck_id).first()
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    db_deck = models.Deck(
        name=deck.name,
        visibility=deck.visibility,
        color=deck.color,
        owner_id=user.id
    )
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)

    # ajoute le deck à la liste des decks de l'utilisateur
    user.decks.append(db_deck)
    db.commit()
    db.refresh(user)

    # ajoute la progression du deck à la liste des progressions de l'utilisateur 
    db_progress = models.DeckProgress(
        user_id=user.id,
        deck_id=db_deck.id,
        progress=0
    )
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)

    user.deck_progress.append(db_progress)
    db.commit()
    db.refresh(user)

    if len(user.decks) == 1:
        user.active_deck_id = db_deck.id
        db.commit()
        db.refresh(user)

    return db_deck

# --- Cards
async def add_card(db: Session, card: schemas.CardCreate, deck_id : models.Deck) -> models.Card:
    """
    Cette fonction permet d'ajouter une carte à un deck
    @param db: Session
    @param card: schemas.CardCreate
    @param deck: models.Deck
    @return models.Card
    """
    db_card = models.Card(
        front_content=card.front_content,
        back_content=card.back_content,
        deck_id=deck_id
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)

    deck = db.query(models.Deck).filter(models.Deck.id == deck_id).first()
    
    # ajoute la carte à la liste des cartes du deck
    deck.cards.append(db_card)
    db.commit()
    db.refresh(deck)

    return db_card

async def update_card(db: Session, card_id: int, state: str, user_id: str) -> models.Card:
    """
    Cette fonction permet de mettre à jour l'état d'une carte
    @param db: Session
    @param card_id: int
    @param state: str
    @param user_id: str
    @return models.Card
    """
    card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    # if card.deck.owner_id != user_id:
    #     raise HTTPException(status_code=403, detail="You are not the owner of the deck")
    card.state = state
    db.commit()
    db.refresh(card)
    return card

# --- Train
async def get_random_card(db: Session, deck_id: int, user: models.User) -> models.Card:
    """
    Cette fonction permet de récupérer une carte aléatoire d'un deck
    @param db: Session
    @param deck_id: int
    @param user: models.User
    @return models.Card
    """
    if deck_id not in [deck.id for deck in user.decks]:
        raise HTTPException(status_code=404, detail="Deck not found")
    deck = db.query(models.Deck).filter(models.Deck.id == deck_id).first()
    size = len(deck.cards)
    if size == 0:
        raise HTTPException(status_code=404, detail="No card in the deck")
    
    # chiffre aléatoire entre 0 et la taille du deck
    random_index = random.randint(0, size-1)
    cards = deck.cards
    return cards[random_index]