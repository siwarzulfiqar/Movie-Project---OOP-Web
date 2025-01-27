from storage_json import JSONStorage  # Use JSON storage
import random

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
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)

    median_rating = sorted_movies[total_movies // 2][1]["rating"] if total_movies % 2 != 0 else (
                                                                                                        sorted_movies[
                                                                                                            total_movies // 2 - 1][
                                                                                                            1][
                                                                                                            "rating"] +
                                                                                                        sorted_movies[
                                                                                                            total_movies // 2][
                                                                                                            1]["rating"]
                                                                                                ) / 2

    best_movie = sorted_movies[0]
    worst_movie = sorted_movies[-1]

    print(f"\nTotal Movies: {total_movies}")
    print(f"Average Rating: {avg_rating:.2f}")
    print(f"Median Rating: {median_rating:.2f}")
    print(f"Best Movie: {best_movie[0]} (Rating: {best_movie[1]['rating']})")
    print(f"Worst Movie: {worst_movie[0]} (Rating: {worst_movie[1]['rating']})")


def random_movie():
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
        return
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
        return
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for title, details in sorted_movies:
        print(f"{title} (Year: {details['year']}, Rating: {details['rating']})")


def generate_website():
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
        return

    try:
        with open("_static/index_template.html", "r") as template_file:
            template_content = template_file.read()

        movies_html = "".join([
            f"""
            <li>
                <h2>{title}</h2>
                <p>Year: {details['year']}</p>
                <p>Rating: {details['rating']}</p>
                <img src=\"{details['poster']}\" alt=\"Poster\">
            </li>
            """
            for title, details in movies.items()
        ])

        html_content = template_content.replace("{{ movies }}", movies_html)

        with open("movies.html", "w") as output_file:
            output_file.write(html_content)

        print("\nWebsite generated as 'movies.html'!")
    except FileNotFoundError:
        print("Template file '_static/index_template.html' not found.")


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
