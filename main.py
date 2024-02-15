from fastapi import FastAPI, HTTPException, Request
from typing import List
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from config.db import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import user_router

app = FastAPI() 
app.add_middleware(ErrorHandler)

app.include_router(user_router)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)

# class JWTBearer(HTTPBearer):
#     async def __call__(self, request: Request):
#         auth = await super().__call__(request)
#         data =  validate_token(auth.credentials)
#         if data['email'] != 'admin@gmail.com':
#             raise HTTPException(status_code=401, detail="Invalid credentials")
    

    
movies = [{
    "id": 1,    
    "title": "The Godfather",
    "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine.",
    "year": 1972,
    "rating": 9.2,
    "category": "Drama"
}, 
{    
    "id": 2,    
    "title": "The Godfather 2",
    "overview": "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands.",
    "year": 1974,
    "rating": 9.0,
    "category": "Accion"
    }]



