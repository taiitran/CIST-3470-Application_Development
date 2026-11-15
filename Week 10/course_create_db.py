import sqlite3

db_connection = sqlite3.connect("course_registration.db")

db_cursor = db_connection.cursor()

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_number TEXT NOT NULL,
        course_name TEXT NOT NULL,
        credits INTEGER,
        semester TEXT NOT NULL
    )
""")

db_connection.close()

print("The course registration database and table are ready.")