from src.Model.Movie import Movie
from src.Service.AppelTMDB import AppelTMDB

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTdjYzRlYzBjY2VjODAyYjhkODNkZGU4NDkyZDcxZCIsIm5iZiI6MTcyNTYzMzI4NS4wODcxMDMsInN1YiI6IjY2ZGIxMjEwOGJhODA5NTQxNTE2MGM4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._FH9kdpEyOIYMwhcSmatqB-fSXewAqX3uGa6Wj0OIDY"
    }


class MovieService:
    movie_db: None

    def __init__(self, movie_db: None):
        self.movie_db = movie_db

    def get_by_id(self, movie_id: int) -> Movie:
        return Movie(id=movie_id, original_title="Un jour peut etre...")
        # return self.movie_db.get_by_id(movie_id)

