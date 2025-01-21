from api_utils import fetch_movie_data
from config import API_KEY
from istorage import IStorage


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
        for title, details in movies.items():
            print(f"{title} (Year: {details['year']}, Rating: {details['rating']})")

    def _command_add_movie(self):
        title = input("Enter the movie title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return

        try:
            # Fetch movie data from the OMDb API
            movie_data = fetch_movie_data(title, API_KEY)
            self._storage.add_movie(
                movie_data["title"],
                movie_data["year"],
                movie_data["rating"],
                movie_data["poster"]
            )
            print(f"Movie '{movie_data['title']}' added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except ConnectionError as e:
            print(f"Error: {e}")

    def _command_delete_movie(self):
        title = input("Enter the title of the movie to delete: ").strip()
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully!")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("0. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
