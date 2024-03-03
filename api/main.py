from fastapi import FastAPI, HTTPException, Depends
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

import tasks
import schemas

# Catégories des endpoints (voir documentations Swagger/redocs)
tags_metadata = [
     {
        "name": "Server",
        "description": "Monitor the server state",
    },
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
]

app = FastAPI(
     title="NotaBene API ",
    openapi_tags=tags_metadata
)
security = HTTPBasic()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Server 
@app.get("/", tags=["Server"])
async def root():
    return {"message": "Hello World"}

@app.get("/unixTimes", tags=["Server"])
async def read_item():
    unix_timestamp = datetime.now().timestamp()
    return {"unixTime": unix_timestamp} 


# --- User 
async def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = await tasks.authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

@app.get("/items/")
async def read_items(current_user: schemas.User = Depends(get_current_user)):
    return {"username": current_user.username}

