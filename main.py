from storage_json import JSONStorage  # Use JSON storage

# from storage_csv import CSVStorage  # Uncomment to use CSV storage

# Choose storage backend
storage = JSONStorage()  # Or CSVStorage()


def display_menu():
    """Display the main menu."""
    print("\nMenu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie rating")


def list_movies():
    """List all movies with their details."""
    movies = storage.list_movies()
    if not movies:
        print("\nNo movies found.")
        return
    print("\nMovies:")
    for title, details in movies.items():
        print(f"{title} (Year: {details['year']}, Rating: {details['rating']})")
        print(f"Poster: {details['poster']}")


def add_movie():
    """Add a new movie."""
    title = input("\nEnter movie title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    try:
        storage.add_movie(title)
    except Exception as e:
        print(f"Error: {e}")


def delete_movie():
    """Delete an existing movie."""
    title = input("\nEnter the title of the movie to delete: ").strip()
    try:
        storage.delete_movie(title)
    except Exception as e:
        print(f"Error: {e}")


def update_movie_rating():
    """Update the rating of an existing movie."""
    title = input("\nEnter the title of the movie to update: ").strip()
    rating = input("Enter new rating (0-10): ").strip()
    try:
        rating = float(rating)
        if not (0 <= rating <= 10):
            print("Rating must be between 0 and 10.")
            return
        storage.update_movie(title, rating)
    except ValueError:
        print("Invalid rating format.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the movie application."""
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
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
