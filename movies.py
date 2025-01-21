from storage_json import JSONStorage  # Use JSON storage

storage = JSONStorage()


def display_menu():
    print("\nMenu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie rating")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Generate website")


def list_movies():
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
    else:
        for title, details in movies.items():
            print(f"{title} (Year: {details['year']}, Rating: {details['rating']})")
            print(f"Poster: {details['poster']}")


def add_movie():
    title = input("\nEnter movie title: ").strip()
    try:
        storage.add_movie(title)
    except Exception as e:
        print(f"Error: {e}")


def delete_movie():
    title = input("\nEnter movie title to delete: ").strip()
    try:
        storage.delete_movie(title)
    except ValueError as e:
        print(e)


def update_movie_rating():
    title = input("\nEnter movie title: ").strip()
    try:
        rating = float(input("Enter new rating (0-10): "))
        storage.update_movie(title, rating)
    except ValueError as e:
        print(e)


def stats():
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
        return
    total_movies = len(movies)
    avg_rating = sum(movie["rating"] for movie in movies.values()) / total_movies
    sorted_ratings = sorted(movie["rating"] for movie in movies.values())
    median_rating = sorted_ratings[total_movies // 2]
    print(f"\nTotal Movies: {total_movies}")
    print(f"Average Rating: {avg_rating:.2f}")
    print(f"Median Rating: {median_rating:.2f}")


def random_movie():
    import random

    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
    else:
        title, details = random.choice(list(movies.items()))
        print(f"\nRandom Movie: {title} (Year: {details['year']}, Rating: {details['rating']})")


def search_movie():
    query = input("\nEnter search query: ").strip().lower()
    movies = storage.list_movies()
    results = {title: details for title, details in movies.items() if query in title.lower()}
    if not results:
        print("No matching movies found.")
    else:
        for title, details in results.items():
            print(f"{title} (Year: {details['year']}, Rating: {details['rating']})")


def movies_sorted_by_rating():
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
    else:
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
        for title, details in sorted_movies:
            print(f"{title} (Year: {details['year']}, Rating: {details['rating']})")


def generate_website():
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
        return
    html_content = """
    <html>
    <head><title>Movies</title></head>
    <body>
        <h1>Movie List</h1>
        <ul>
    """
    for title, details in movies.items():
        html_content += f"""
            <li>
                <h2>{title}</h2>
                <p>Year: {details['year']}</p>
                <p>Rating: {details['rating']}</p>
                <img src="{details['poster']}" alt="Poster">
            </li>
        """
    html_content += """
        </ul>
    </body>
    </html>
    """
    with open("movies.html", "w") as file:
        file.write(html_content)
    print("\nWebsite generated as 'movies.html'!")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie_rating()
        elif choice == "5":
            stats()
        elif choice == "6":
            random_movie()
        elif choice == "7":
            search_movie()
        elif choice == "8":
            movies_sorted_by_rating()
        elif choice == "9":
            generate_website()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
