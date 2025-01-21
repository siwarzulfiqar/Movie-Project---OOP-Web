import json
from istorage import IStorage
from api_utils import fetch_movie_data

MOVIE_FILE = "movies.json"
OMDB_API_KEY = "9282927"  # MY OMDB API key


class JSONStorage(IStorage):
    def __init__(self):
        self.file = MOVIE_FILE

    def _load_movies(self):
        """Load movies from the JSON file."""
        try:
            with open(self.file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_movies(self, movies):
        """Save movies to the JSON file."""
        with open(self.file, "w") as file:
            json.dump(movies, file, indent=4)

    def list_movies(self):
        """Returns all movies from the JSON file."""
        return self._load_movies()

    def add_movie(self, title):
        """
        Adds a new movie to the JSON file by fetching details from the OMDB API.
        """
        movies = self._load_movies()
        if title in movies:
            raise ValueError(f"Movie '{title}' already exists.")
        try:
            movie = fetch_movie_data(title, OMDB_API_KEY)
            movies[movie["title"]] = {
                "year": movie["year"],
                "rating": movie["rating"],
                "poster": movie["poster"],
            }
            self._save_movies(movies)
            print(f"Movie '{movie['title']}' added successfully!")
        except Exception as e:
            print(e)

    def delete_movie(self, title):
        """
        Deletes a movie from the JSON file.
        """
        movies = self._load_movies()
        if title not in movies:
            raise ValueError(f"Movie '{title}' not found.")
        del movies[title]
        self._save_movies(movies)
        print(f"Movie '{title}' deleted successfully!")

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the JSON file.
        """
        movies = self._load_movies()
        if title not in movies:
            raise ValueError(f"Movie '{title}' not found.")
        movies[title]["rating"] = rating
        self._save_movies(movies)
        print(f"Rating for '{title}' updated successfully!")
