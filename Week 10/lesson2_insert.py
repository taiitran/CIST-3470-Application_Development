import sqlite3

db_connection = sqlite3.connect("movie_library.db")

db_cursor = db_connection.cursor()

title = input("Movie title: ")
year = int(input("Release year: "))
minutes = int(input("Running time in minutes: "))

# Add a movie
db_cursor.execute("""
    INSERT INTO movies (title, year, minutes)
    VALUES (?, ?, ?)
""", (title, year, minutes))

# commit() saves pending changes in a transaction.
#  We will use it after adding, updating, or deleting records.
db_connection.commit()

print("This movie is added.")
print("\nAll the movies in the database:")

# Retrieve all movies.
# Where are the results?
#  The results are managed internally by SQLite and accessed through my_cursor.
db_cursor.execute("""
    SELECT movie_id, title, year, minutes
    FROM movies
    ORDER BY movie_id
""")

# fetchall() retrieves all remaining query-result rows as a list of tuples.
# In this example, we have not fetched anything yet.
#  So, fetchall() gets all the query-result rows.
movies = db_cursor.fetchall()
db_connection.close()

for movie_id, title, year, minutes in movies:
    print(f"{movie_id}. {title} ({year}) - {minutes} minutes")
