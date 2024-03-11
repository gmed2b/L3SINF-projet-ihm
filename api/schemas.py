
# --- Importation des modules
# pydantic est utilisé pour la validation des données
from pydantic import BaseModel

# --- Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

# --- User schemas
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    rgpd: bool

# UserCreate est utilisé pour la création d'un utilisateur il contient un champ password + les champs de UserBase
class UserCreate(UserBase):
    password: str

# User est utilisé pour la lecture d'un utilisateur il contient un champ id + les champs de UserBase
class User(UserBase):
    id: int
    class Config:
        orm_mode = True
