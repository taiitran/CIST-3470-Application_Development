import sqlite3

db_connection = sqlite3.connect("movie_library.db")

db_cursor = db_connection.cursor()

movie_id = int(input("Enter a movie ID: "))

# Search for the movie.
db_cursor.execute("""
    SELECT movie_id, title, year, minutes
    FROM movies
    WHERE movie_id = ?
""", (movie_id,))

# Retrieve the matching row, if any.
movie = db_cursor.fetchone()

db_connection.close()

# Display the result.
if movie is None:
    print("Movie not found.")
else:
    movie_id, title, year, minutes = movie
    print(f"{movie_id}. {title} ({year}) - {minutes} minutes")
