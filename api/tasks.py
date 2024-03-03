from typing import Optional
import schemas

async def authenticate_user(username: str, password: str):
    if username == "u" and password == "p":
        return schemas.User(username=username, password=password)
    return None

