from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of all movies.
        Each movie is represented as a dictionary.
        """
        pass

    @abstractmethod
    def add_movie(self, title):
        """
        Fetches movie details from the API and adds the movie to the storage.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the storage.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the storage.
        """
        pass
