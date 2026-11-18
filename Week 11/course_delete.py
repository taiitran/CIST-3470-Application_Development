import sqlite3

course_id = int(input("Enter the course ID to delete: "))

db_connection = sqlite3.connect("course_registration.db")

db_cursor = db_connection.cursor()

db_cursor.execute("""
    DELETE FROM courses
    WHERE course_id = ?
""", (course_id,))

deleted_count = db_cursor.rowcount

db_connection.commit()
db_connection.close()

if deleted_count == 0:
    print("Course not found.")
else:
    print("Course deleted.")