from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con FastAPI"  # Agregando título 
app.version = "2.3"                      # Agregando version


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
def create_movie(id: int = Body(), title: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    
    movies.append(
        {
        "id": id, 
        "title": title, 
        "overview": overview, 
        "year": year, 
        "rating": rating, 
        "category": category
        }
    )
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    

    for item in movies:
        if item["id"]==id:
            item["title"]: title
            item["overview"]: overview
            item["year"]: year
            item["rating"]: rating
            item["category"]: category
            return movies


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    

    for item in movies:
        if item["id"]==id:
            movies.remove(item)
            return movies