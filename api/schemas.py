
# --- Importation des modules
# pydantic est utilisé pour la validation des données
from pydantic import BaseModel
from typing import List, Optional

# --- Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str = None

# --- User schemas
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    rgpd: bool
    following: List["User"] = []
    decks: List["Deck"] = []
    deck_progress: List["DeckProgress"] = []
    
# UserCreate est utilisé pour la création d'un utilisateur, il contient un champ password + les champs de UserBase
class UserCreate(UserBase):
    password: str

# User est utilisé pour la lecture d'un utilisateur, il contient un champ id + les champs de UserBase
class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# --- Card schemas
class CardBase(BaseModel):
    front_content: str
    back_content: str
    state: str = "not memorized" or "memorized" or "in progress"

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int
    deck_id: int

    class Config:
        orm_mode = True

# --- Tag schemas
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True

# --- Deck schemas
class DeckBase(BaseModel):
    name: str
    visibility: str = "private" or "public" or "friends"
    color: str = "blue" or "green" or "red" or "yellow" or "purple" or "pink" or "orange"
    cards : List[Card] = []
    tags : List[Tag] = []

class DeckCreate(DeckBase):
    pass

class Deck(DeckBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# --- DeckProgress schemas
class DeckProgressBase(BaseModel):
    progress: int

class DeckProgressCreate(DeckProgressBase):
    pass

class DeckProgress(DeckProgressBase):
    user_id: int
    deck_id: int

    class Config:
        orm_mode = True

# --- UserDeck schemas
class UserDeckBase(BaseModel):
    user_id: int
    deck_id: int

class UserDeckCreate(UserDeckBase):
    pass

class UserDeck(UserDeckBase):
    class Config:
        orm_mode = True
