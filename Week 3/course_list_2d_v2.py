import csv 

FILE_NAME = "course_list.csv"

def display_menu():
    print("The course List program V2")
    print("COMMAND MENU")
    print("list - List all courses")
    print("add - Add a course")
    print("del - Delete a course")
    print("exit - Exit program")
    print()

def write_courses(my_courses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(my_courses)

def read_courses():
    my_courses = []

    with open(FILE_NAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            my_courses.append(row)
        
    return my_courses

def list_course(my_course_2dlist):
    if len(my_course_2dlist) == 0:
        print("There are no courses in the list.\n")
    else:
        my_course_number = 1
        for course in my_course_2dlist:
            print(my_course_number, course[0], course[1], course[2])
            my_course_number = my_course_number + 1
        print()

def add_course(my_course_2dlist):
    number = input("Course number: ")
    name = input("Course name: ")
    credit = input("Credits: ")
    my_course = [number, name, credit]
    my_course_2dlist.append(my_course)
    write_courses(my_course_2dlist)
    print(f"{my_course[1]} was added.\n")

def delete_course(my_course_2dlist):
    my_course_number = int(input("Enter Course No. to Delete: "))
    if my_course_number < 1 or my_course_number > len(my_course_2dlist):
        print("Invalid course number.\n")
    else:
        my_course = my_course_2dlist.pop(my_course_number - 1)
        write_courses(my_course_2dlist)
        print(f"{my_course[1]} was deleted.\n")

def main():
    display_menu()
    course_list = read_courses()

    while True:
        command = input("Command: ")

        if command.lower() == "exit":
            break

        if command.lower() == "list":
            list_course(course_list)
        elif command.lower() == "add":
            add_course(course_list)
        elif command.lower() == "del":
            delete_course(course_list)
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
    main()


