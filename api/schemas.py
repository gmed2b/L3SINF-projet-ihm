
# --- Importation des modules
# pydantic est utilisé pour la validation des données
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

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
        from_attributes = True

# --- Card's state 
#https://stackoverflow.com/questions/71926005/fastapi-how-to-use-enums-for-the-basemodel-schema
class State(str,Enum):
    not_memorized = "not memorized"
    memorized = "memorized"
    in_progress = "in progress"

# --- Card schemas
class CardBase(BaseModel):
    front_content: str
    back_content: str
    state: State = "not memorized"

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int
    deck_id: int

    class Config:
        from_attributes = True

# --- Tag schemas
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True

# --- Deck schemas

# --- Deck's visibility
class Visibility(str,Enum):
    private = "private"
    public = "public"
    friends = "friends"

# --- Deck's color
class Color(str,Enum):
    blue = "blue"
    green = "green"
    red = "red"
    yellow = "yellow"
    purple = "purple"
    pink = "pink"
    orange = "orange"

class DeckBase(BaseModel):
    name: str
    visibility: Visibility = "private"
    color: Color = "blue"
    cards : List[Card] = []
    tags : List[Tag] = []

class DeckCreate(DeckBase):
    pass

class Deck(DeckBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# --- DeckProgress schemas
class DeckProgressBase(BaseModel):
    progress: int

class DeckProgressCreate(DeckProgressBase):
    pass

class DeckProgress(DeckProgressBase):
    user_id: int
    deck_id: int

    class Config:
        from_attributes = True

# --- UserDeck schemas
class UserDeckBase(BaseModel):
    user_id: int
    deck_id: int

class UserDeckCreate(UserDeckBase):
    pass

class UserDeck(UserDeckBase):
    class Config:
        from_attributes = True
