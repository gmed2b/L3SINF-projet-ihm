# --- Importation des modules
# sqlalchemy est utilisé pour la gestion de la base de données, cela permet de créer des modèles de données, de les manipuler, etc.
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# sqlalchemy.orm est utilisé pour la session de la base de données, cela permet d'accéder à la base de données, de la lire et de l'écrire, etc.
from sqlalchemy.orm import relationship
# sqlalchemy.ext.declarative est utilisé pour la déclaration de la base de données
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
    active_deck_id = Column(Integer, ForeignKey("Decks.id"))

    # Relation: Un utilisateur peut suivre plusieurs autres utilisateurs
    following = relationship("User", secondary="user_followers", 
                             primaryjoin="User.id==UserFollowers.user_id",
                             secondaryjoin="User.id==UserFollowers.following_id",
                             backref="followers")
    
    # Relation: Un utilisateur peut posséder plusieurs decks)
    decks = relationship("Deck", back_populates="owner", 
                         primaryjoin="User.id==Deck.owner_id") 

    # Relation: La progression du deck spécifique à chaque utilisateur
    deck_progress = relationship("DeckProgress", back_populates="user")



#--- Deck
class Deck(Base):
    __tablename__ = "Decks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    visibility = Column(String, default="private")
    color = Column(String, default="blue")

    # Relation: Un deck peut être possédé par plusieurs utilisateurs
    owner_id = Column(Integer, ForeignKey("Users.id"))
    owner = relationship("User", back_populates="decks", 
                        primaryjoin="Deck.owner_id==User.id")  # Spécifier la jointure explicite ici
    # Relation: Un deck peut contenir plusieurs cartes
    cards = relationship("Card", back_populates="deck")
    # Relation: Un deck est associé à un seul tag
    tag_id = Column(Integer, ForeignKey("Tags.id"))
    tag = relationship("Tag", back_populates="decks")

    # Relation: La progression du deck spécifique à chaque utilisateur
    user_progress = relationship("DeckProgress", back_populates="deck")



#--- Card
class Card(Base):
    __tablename__ = "Cards"
    id = Column(Integer, primary_key=True, index=True)
    front_content = Column(String)
    back_content = Column(String)
    state = Column(String, default="not memorized")
    # Relation: Une carte est dans un seul deck
    deck_id = Column(Integer, ForeignKey("Decks.id"))
    deck = relationship("Deck", back_populates="cards")


#--- Tag
class Tag(Base):
    __tablename__ = "Tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # Relation: Un tag est associé à plusieurs decks
    decks = relationship("Deck", back_populates="tag")


# --- DeckProgress
# Table de liaison pour la relation entre decks et utilisateurs avec la progression spécifique de chaque utilisateur
class DeckProgress(Base):
    __tablename__ = "deck_progress"
    user_id = Column(Integer, ForeignKey("Users.id"), primary_key=True)
    deck_id = Column(Integer, ForeignKey("Decks.id"), primary_key=True)
    progress = Column(Integer)  # La progression du deck pour cet utilisateur

    # Relation: Un enregistrement de progression appartient à un utilisateur
    user = relationship("User", back_populates="deck_progress")
    # Relation: Un enregistrement de progression appartient à un deck
    deck = relationship("Deck", back_populates="user_progress")


# --- UserFollowers
# Table de liaison pour la relation Many-to-Many entre utilisateurs
class UserFollowers(Base):
    __tablename__ = "user_followers"
    user_id = Column(Integer, ForeignKey("Users.id"), primary_key=True)
    following_id = Column(Integer, ForeignKey("Users.id"), primary_key=True)
