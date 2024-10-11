import requests




headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMTdjYzRlYzBjY2VjODAyYjhkODNkZGU4NDkyZDcxZCIsIm5iZiI6MTcyNTYzMzI4NS4wODcxMDMsInN1YiI6IjY2ZGIxMjEwOGJhODA5NTQxNTE2MGM4ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._FH9kdpEyOIYMwhcSmatqB-fSXewAqX3uGa6Wj0OIDY"
    }



def rechercher_film(query, language, primary_release_year, page, region, year):
    payload = {'query': query,
                'language': language,
                'primary_release_year': primary_release_year,
                'page': page,
                'region': region,
                'year': year}
    response = requests.get('https://api.themoviedb.org/3/search/movie?',
    params=payload, headers=headers)
    data = response.json()
    films = data.get('results', [])
    resultats = [(film['id'], film['title']) for film in films]
    return resultats


print(rechercher_film("Le parrain", "fr-FR", None, "1", None, None))


def obtenir_info_film(film_id,language):
    url = f'https://api.themoviedb.org/3/movie/{film_id}'
    params = {
    'language': language
    }
    response = requests.get(url, params=params,headers=headers)
    data = response.json()
    return {
        'Titre': data.get('title', 'Non disponible'),
        'Titre original': data.get('original_title', 'Non disponible'),
        'Date de sortie': data.get('release_date', 'Non disponible'),
        'Durée': f"{data.get('runtime', 'Non disponible')} minutes",
        'Genre(s)': ', '.join(genre['name'] for genre in data.get('genres', [])),
        'Résumé': data.get('overview', 'Non disponible'),
        'Budget': f"{data.get('budget', 0):,} USD",
        'Revenus': f"{data.get('revenue', 0):,} USD",
        'Langue originale': data.get('original_language', 'Non disponible'),
        'Production(s)': ', '.join(production['name'] for production in data.get('production_companies', [])),
        'Pays de production': ', '.join(production['name'] for production in data.get('production_countries', [])),
    }

print(obtenir_info_film(238,'fr-FR'))