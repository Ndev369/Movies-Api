from pydantic import BaseModel, Field
from fastapi.security import HTTPBearer
from fastapi import Request
from fastapi import HTTPException
from utils.jwt_manager import validate_token



class User(BaseModel):
    email:str = Field(example="admin@gmail.com")
    password:str = Field(min_length=6, max_length=16, example="123456")
    

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data =  validate_token(auth.credentials)
        if data['email'] != 'admin@gmail.com':
            raise HTTPException(status_code=401, detail="Invalid credentials")
    