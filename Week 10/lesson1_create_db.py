# Imports Python’s sqlite3 module,
#  which provides the functions and classes needed to work with an SQLite database.
import sqlite3

# Creates a connection object. The object opens movies.db.
#  If the database file cannot be found, it creates the file first.
db_connection = sqlite3.connect("movie_library.db")

# Uses the cursor() method to create a cursor object.
#  We use this object to execute SQL statements and retrieve query results.
db_cursor = db_connection.cursor()

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        year INTEGER,
        minutes INTEGER
    )
""")

# commit() saves pending changes in a transaction.
#  We will use it after adding, updating, or deleting records.
#  So in this example, commit() can be omiited.

## db_connection.commit()
db_connection.close()

print("The movie database and table are ready.")
