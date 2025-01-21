import requests


def fetch_movie_data(title, api_key):
    """
    Fetches movie data from the OMDb API using the provided title.

    Args:
        title (str): The title of the movie to fetch.
        api_key (str): Your OMDb API key.

    Returns:
        dict: A dictionary containing movie data (title, year, rating, poster).

    Raises:
        ValueError: If the movie is not found.
        ConnectionError: If there's an issue connecting to the API.
    """
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            return {
                "title": data.get("Title"),
                "year": int(data.get("Year")),
                "rating": float(data.get("imdbRating")),
                "poster": data.get("Poster"),
            }
        else:
            raise ValueError(f"Movie '{title}' not found in OMDb database.")
    else:
        raise ConnectionError("Failed to connect to OMDb API.")
