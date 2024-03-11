# --- Importation des modules
# sqlalchemy est utilisé pour la gestion de la base de données, cela permet de créer des modèles de données, de les manipuler, etc.
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# --- User model
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String) 
    rgpd = Column(Boolean)
