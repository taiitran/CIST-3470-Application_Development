program_name = "Grade Calculator for the Stockton University"
developer_name = "Tai Tran"
date = "11/02/2026"
print(f"Program name: {program_name}\n"
      f"Developer name: {developer_name}\n"
        f"Date: {date}\n")

print("The program calculates a grade for the standard letter grading mode")
number_grade = float(input("Enter number grade: "))

if number_grade >= 93:
    letter_grade = "A"
elif number_grade >= 90:
    letter_grade = "A-"
elif number_grade >= 87:
    letter_grade = "B+"
elif number_grade >= 83:
    letter_grade = "B"
elif number_grade >= 80:
    letter_grade = "B-"
elif number_grade >= 77:
    letter_grade = "C+"
elif number_grade >= 73:
    letter_grade = "C"
elif number_grade >= 70:
    letter_grade = "C-"
elif number_grade >= 67:
    letter_grade = "D+"
elif number_grade >= 63:
    letter_grade = "D"
elif number_grade >= 60:
    letter_grade = "D-"
else:
    letter_grade = "F"

print()
print("Final grade on the transcript:", letter_grade)

