from src.Model.Movie import Movie

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTdjYzRlYzBjY2VjODAyYjhkODNkZGU4NDkyZDcxZCIsIm5iZiI6MTcyNTYzMzI4NS4wODcxMDMsInN1YiI6IjY2ZGIxMjEwOGJhODA5NTQxNTE2MGM4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._FH9kdpEyOIYMwhcSmatqB-fSXewAqX3uGa6Wj0OIDY"
    }


class MovieService:
    movie_db: None

    def __init__(self, movie_db: None):
        self.movie_db = movie_db

    def get_by_id(self, movie_id: int) -> Movie:
        url = f'https://api.themoviedb.org/3/movie/{film_id}'
        response = requests.get(url,headers=headers)
        data = response.json()
        return Movie(id=movie_id, original_title=data.get('original_title', 'Non disponible'))
        # return self.movie_db.get_by_id(movie_id)
