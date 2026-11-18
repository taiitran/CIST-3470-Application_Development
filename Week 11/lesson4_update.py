import sqlite3

db_connection = sqlite3.connect("movies_library.db")

db_cursor = db_connection.cursor()

movie_id = int(input("Enter the movie ID to update: "))
new_year = int(input("Enter the corrected release year: "))
new_minutes = int(input("Enter the new running time in minutes: "))

# Update the selected movie.
db_cursor.execute("""
    UPDATE movies
    SET year = ?, minutes = ?
    WHERE movie_id = ?
""", (new_year, new_minutes, movie_id))

# rowcount is an attribute.
# It tells you how many rows were affected
#  by the most recent UPDATE executed through that cursor.
# rowcount, although optional, is mainly useful for INSERT, UPDATE, and DELETE statements.
#  It is especially helpful for updates and deletions,
#  because a statement can execute successfully while matching no records.
# Read rowcount before executing another SQL statement through that cursor.
#  rowcount does not confirm that changes have been saved; you still need commit().
updated_count = db_cursor.rowcount

# Save the update and close the connection.
db_connection.commit()
db_connection.close()

if updated_count == 0:
    print("Movie not found.")
else:
    print("Movie updated.")
