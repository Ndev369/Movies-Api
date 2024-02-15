from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token,create_token
from fastapi import Request
from schemas.user import User, JWTBearer


user_router = APIRouter()


@user_router.post('/login',tags=['Auth'], status_code=status.HTTP_200_OK)
async def login(user:User):
    if user.email == 'admin@gmail.com' and user.password == '123456':
        token:str = create_token(user.model_dump())
        return JSONResponse(content=token) 
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
