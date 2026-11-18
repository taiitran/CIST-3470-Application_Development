import sqlite3

db_connection = sqlite3.connect("course_registration.db")

db_cursor = db_connection.cursor()

course_id = int(input("Enter the course ID to update: "))
new_credits = int(input("Enter the new number of credits for the course: "))
new_semester = input("Enter the new semester for the course: ")

db_cursor.execute("""
    UPDATE courses
    SET credits = ?, semester = ?
    WHERE course_id = ?
""", (new_credits, new_semester, course_id))

updated_count = db_cursor.rowcount

db_connection.commit()
db_connection.close()

if updated_count == 0:
    print("Course not found.")
else:
    print("Course updated.")