import sqlite3

def get_movies(my_db_connection):
    my_cursor = my_db_connection.cursor()
    my_cursor.execute("""
        SELECT movie_id, title, year, minutes
        FROM movies
        ORDER BY movie_id
    """)
    my_movies = my_cursor.fetchall()
    my_cursor.close()
    return my_movies

def add_movie(my_db_connection, my_db_title, my_db_year, my_db_minutes):
    my_cursor = my_db_connection.cursor()
    my_cursor.execute("""
        INSERT INTO movies (title, year, minutes)
        VALUES (?, ?, ?)
    """, (my_db_title, my_db_year, my_db_minutes))
    inserted_count = my_cursor.rowcount
    my_db_connection.commit()
    my_cursor.close()
    return inserted_count

def find_movie(my_db_connection, my_db_movie_id):
    my_cursor = my_db_connection.cursor()
    my_cursor.execute("""
        SELECT movie_id, title, year, minutes
        FROM movies
        WHERE movie_id = ?
    """, (my_db_movie_id,))
    my_movie = my_cursor.fetchone()
    my_cursor.close()
    return my_movie

def update_movie(my_db_connection, my_db_movie_id, my_db_new_year, my_db_new_minutes):
    my_cursor = my_db_connection.cursor()
    my_cursor.execute("""
        UPDATE movies
        SET year = ?, minutes = ?
        WHERE movie_id = ?
    """, (my_db_new_year, my_db_new_minutes, my_db_movie_id))
    updated_count = my_cursor.rowcount
    my_db_connection.commit()
    my_cursor.close()
    return updated_count

def delete_movie(my_db_connection, my_db_movie_id):
    my_cursor = my_db_connection.cursor()
    my_cursor.execute("""
        DELETE FROM movies
        WHERE movie_id = ?
    """, (my_db_movie_id,))
    deleted_count = my_cursor.rowcount
    my_db_connection.commit()
    my_cursor.close()
    return deleted_count

def display_menu():
    print("THE MOVIE LIST PROGRAM\n")
    print("COMMAND MENU")
    print("list   - List all movies")
    print("add    - Add a movie")
    print("find   - Find a movie")
    print("update - Update a movie's year and running time")
    print("delete - Delete a movie")
    print("exit   - Exit the program")

def display_a_movie(my_movie):
    movie_id, title, year, minutes = my_movie
    print(f"{movie_id}. {title} ({year}) - {minutes} minutes")

def list_movies(my_connection):
    movies = get_movies(my_connection)
    if not movies:
        print("No movies found.")
    else:
        for movie in movies:
            display_a_movie(movie)

def add_movie_ui(my_connection):
    title = input("Title: ")
    year = int(input("Release year: "))
    minutes = int(input("Running time in minutes: "))
    added_count = add_movie(my_connection, title, year, minutes)
    print(f"{added_count} movie(s) added.")

def find_movie_ui(my_connection):
    movie_id = int(input("Movie ID: "))
    movie = find_movie(my_connection, movie_id)
    if movie is None:
        print("Movie not found.")
    else:
        display_a_movie(movie)

def update_movie_ui(my_connection):
    movie_id = int(input("Movie ID: "))
    movie = find_movie(my_connection, movie_id)
    if movie is None:
        print("Movie not found.")
        return

    display_a_movie(movie)
    new_year = int(input("Corrected release year: "))
    new_minutes = int(input("Corrected running time in minutes: "))
    updated_count = update_movie(my_connection, movie_id, new_year, new_minutes)
    print(f"{updated_count} movie(s) updated.")

def delete_movie_ui(my_connection):
    movie_id = int(input("Movie ID: "))
    movie = find_movie(my_connection, movie_id)
    if movie is None:
        print("Movie not found.")
        return

    display_a_movie(movie)
    confirmation = input("Delete this movie? (y/n): ").strip().lower()
    if confirmation == "y":
        deleted_count = delete_movie(my_connection, movie_id)
        print(f"{deleted_count} movie(s) deleted.")
    else:
        print("Deletion canceled.")

def main():
    db_connection = sqlite3.connect("movies_library.db")
    display_menu()
    try:
        while True:
            command = input("\nCommand: ").strip().lower()
            if command == "exit":
                break
            if command == "list":
                list_movies(db_connection)
            elif command == "add":
                add_movie_ui(db_connection)
            elif command == "find":
                find_movie_ui(db_connection)
            elif command == "update":
                update_movie_ui(db_connection)
            elif command == "delete":
                delete_movie_ui(db_connection)
            else:
                print("Not a valid command. Please try again.\n")
    finally:
        db_connection.close()

    print("Bye!")


if __name__ == "__main__":
    main()
