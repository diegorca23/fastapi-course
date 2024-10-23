from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "Mi aplicación con FastAPI"  # Agregando título 
app.version = "2.3"                      # Agregando version


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float
    category: str

    class Config:
        shchema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2022,
                "rating": 10.0,
                "category":"Accion"
            }
        }


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Dvatar",
        "overview": "En un horripilante planeta llamado Pandorus viven los Nie'vi, seres que...",
        "year": "2019",
        "rating": 6.8,
        "category": "Romance-Terror"
    }
]


@app.get('/', tags=['home']) # con tags=["home"] agregando etiqueta de rutas para la documentación
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    """Retorna la lista de todas las películas"""

    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    """Retorna una elemento de la lista de películas que conincide con el parámetro de la ruta"""

    for item in movies:
        if item["id"]==id:
            return item

    return []

@app.get('/movies/', tags=['movies'])
def get_movie_by_category(category: str, year: int):
    """
    Retorna una elemento de la lista de películas que conincide con el parámetro query de "category"
    
    Para diferenciarse y no sobre-escribir la ruta movies de get_movies() agregamos el "/" al final

    """

    filtered_by_category = [movie for movie in movies if movie["category"] == category]
    
    return filtered_by_category

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie:Movie):
    

    for item in movies:
        if item["id"]==id:
            item["title"]: movie.title
            item["overview"]: movie.overview
            item["year"]: movie.year
            item["rating"]: movie.rating
            item["category"]: movie.category
            return movies


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    

    for item in movies:
        if item["id"]==id:
            movies.remove(item)
            return movies