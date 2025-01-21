import json
import requests

# OMDB API Configuration
OMDB_API_KEY = "9282927"
OMDB_API_URL = "http://www.omdbapi.com/"

# Path to the JSON file
MOVIE_FILE = "movies.json"


def load_movies():
    """Load movies from the JSON file."""
    try:
        with open(MOVIE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_movies(movies):
    """Save movies to the JSON file."""
    with open(MOVIE_FILE, "w") as file:
        json.dump(movies, file, indent=4)


def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.
    """
    return load_movies()


def fetch_movie_from_api(title):
    """Fetch movie details from the OMDB API."""
    params = {"t": title, "apikey": OMDB_API_KEY}
    response = requests.get(OMDB_API_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch movie: HTTP {response.status_code}")

    movie = response.json()
    if movie.get("Response") == "False":
        raise Exception(f"Movie not found: {movie.get('Error')}")

    return {
        "title": movie.get("Title"),
        "year": int(movie.get("Year", 0)),
        "rating": float(movie.get("imdbRating", 0)),
        "poster": movie.get("Poster"),
    }


def add_movie(title):
    """
    Adds a movie to the movies database.
    Fetches movie details from the API and saves them to the JSON file.
    """
    movies = load_movies()
    if title in movies:
        print(f"Movie '{title}' already exists.")
        return

    try:
        movie = fetch_movie_from_api(title)
        movies[movie["title"]] = {
            "year": movie["year"],
            "rating": movie["rating"],
            "poster": movie["poster"],
        }
        save_movies(movies)
        print(f"Movie '{movie['title']}' added successfully!")
    except Exception as e:
        print(e)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    """
    movies = load_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)
        print(f"Movie '{title}' deleted successfully!")
    else:
        print(f"Movie '{title}' not found.")


def update_movie(title, rating):
    """
    Updates a movie's rating in the movies database.
    """
    movies = load_movies()
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)
        print(f"Rating for '{title}' updated successfully!")
    else:
        print(f"Movie '{title}' not found.")