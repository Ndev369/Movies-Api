from fastapi import APIRouter, HTTPException, Path, Query, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.db import Session
from models.movie import Movie as MovieModel
from pydantic import Field, BaseModel
from typing import Optional, List
from routers.users import JWTBearer
from schemas.movie import Movies


movie_router = APIRouter()



@movie_router.get('/movies', tags=["Get Movies"], response_model=list[Movies],dependencies=[Depends(JWTBearer())])
async def get_movies() -> list[Movies]:
    db_session = Session()
    result = db_session.query(MovieModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@movie_router.get('/movies/{id}/', tags=['Get Movies'],response_model=Movies,dependencies=[Depends(JWTBearer())])
async def get_movie_id(id: int = Path(ge=1,le=1000)) -> Movies:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
 
@movie_router.get('/movies/', tags=['Get Movies'], response_model=list[Movies],dependencies=[Depends(JWTBearer())])
async def get_movie_categories(category: str = Query(min_length=3, max_length=17))-> list[Movies]:
    db=Session()
    result = db.query(MovieModel).filter(MovieModel.category == category.capitalize()).all()
    if not result:
        raise HTTPException(status_code=404, detail="Category not found")
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@movie_router.post('/movies', tags=['Create Movie'], response_model=dict, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
async def create_movie(movie:Movies) -> dict:
    try:
        db = Session()
        new_movie = MovieModel(**movie.model_dump())
        db.add(new_movie)
        db.commit()
        return JSONResponse(content={"message":"Movie created"})    
    except:
        raise HTTPException(status_code=404, detail="Movie not added")

@movie_router.put('/movies/{id}/', tags=['Update Movie'] , response_model=dict, status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def update_movie(id: int, movie:Movies) -> dict:
    db=Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category    
    db.commit()
    return JSONResponse(content={"message":"Movie updated"})

@movie_router.delete('/movies/{id}', tags=['Delete Movie'], response_model=dict, status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def delete_movie(id:int)-> dict:
    db=Session()
    result = db.query(MovieModel).filter(MovieModel.id== id).delete(synchronize_session=False)
    db.commit()
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content={"message":"Movie deleted"})
