from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas
import tasks
import database

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_all_users(db: Session):
    return db.query(models.User).all()

async def add_user(db: Session, user: schemas.UserCreate):
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
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not tasks.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = tasks.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}