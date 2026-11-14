import sqlite3

db_connection = sqlite3.connect("course_registration.db")

db_cursor = db_connection.cursor()

course_prefix = input("Course Prefix: ")
course_number = input("Course Number: ")
course_number = f"{course_prefix.upper()} {course_number}"
course_name = input("Course Name: ")
credits = int(input("Credits: "))
semester = input("Semester: ")

db_cursor.execute("""
    INSERT INTO courses (course_number, course_name, credits, semester)
    VALUES (?, ?, ?, ?)
""", (course_number, course_name, credits, semester))

db_connection.commit()

print("The course was added.")
print("\nAll the courses in the database:")

db_cursor.execute("""
    SELECT course_id, course_number, course_name, credits, semester
    FROM courses
    ORDER BY course_id
""")

courses = db_cursor.fetchall()
db_connection.close()

for course_id, course_number, course_name, credits, semester in courses:
    print(f"{course_id}. {course_number} - {course_name} ({credits} credits) - {semester}")