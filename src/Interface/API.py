import uvicorn
from fastapi import FastAPI, HTTPException, status

from src.Model.Movie import Movie
from src.Service.MovieService import MovieService
from src.Service.AppelTMDB import AppelTMDB

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTdjYzRlYzBjY2VjODAyYjhkODNkZGU4NDkyZDcxZCIsIm5iZiI6MTcyNTYzMzI4NS4wODcxMDMsInN1YiI6IjY2ZGIxMjEwOGJhODA5NTQxNTE2MGM4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._FH9kdpEyOIYMwhcSmatqB-fSXewAqX3uGa6Wj0OIDY"
    }


def run_app(movie_service: MovieService):
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/movies/{tmdb_id}", status_code=status.HTTP_200_OK)
    def get_movie_by_id(tmdb_id: int) -> Movie:
        try:
            my_movie: Movie = movie_service.get_by_id(tmdb_id)
            return my_movie
        except FileNotFoundError:
            raise HTTPException(
                status_code=404,
                detail="Movie with id [{}] not found".format(tmdb_id),
            ) from FileNotFoundError
        except Exception as error:
            raise HTTPException(status_code=400, detail="Invalid request") from error

    @app.get("/info/{id_film}")
    def rechercher_film(id_film):
        return AppelTMDB(headers).obtenir_info_film(id_film)


    uvicorn.run(app, port=8000, host="localhost")
