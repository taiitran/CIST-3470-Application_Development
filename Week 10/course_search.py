import sqlite3

db_connection = sqlite3.connect("course_registration.db")

db_cursor = db_connection.cursor()

course_id = int(input("Enter a course ID: "))

db_cursor.execute("""
    SELECT course_id, course_number, course_name, credits, semester
    FROM courses
    WHERE course_id = ?
""", (course_id,))

course = db_cursor.fetchone()
db_connection.close()

if course is None:
    print("Course not found.")
else:
    course_id, course_number, course_name, credits, semester = course
    print(f"{course_id}. {course_number} - {course_name} ({credits} credits) - {semester}")