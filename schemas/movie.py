from pydantic import BaseModel, Field
from typing import Optional




class Movies(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=20)
    overview: str = Field(min_length=1, max_length=300)
    year: int = Field(ge=1900,le=2024)
    rating: float = Field(ge=0.0,le=10.0)
    category: str = Field(min_length=3, max_length=17)
    
    model_config = {
        'json_schema_extra': {
            "example": {
                    "id": 1,
                    "title": "The Godfather",  
                    "overview": "The aging patriarch of stine empire to his reluctant son.",
                    "year": 1972,
                    "rating": 9.2,
                    "category": "Drama"
            }
            
        }
    }
