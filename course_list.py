def display_menu():
    print("The Course List program")
    print()
    print("COMMAND MENU")
    print("list - List all courses")
    print("add - Add a course")
    print("del - Delete a course")
    print("exit - Exit program")
    print()

def list_course(my_course_list):
    if len(my_course_list) == 0:
        print("There are no courses in the list.\n")
    else:
        my_course_number = 1
        for course in my_course_list:
            print(my_course_number, course)
            my_course_number = my_course_number + 1
        print()

def add_course(my_course_list):
    my_movie = input("Course: ")
    my_course_list.append(my_movie)
    print(f"{my_movie} was added.\n")

def delete_course(my_course_list):
    my_course_number = int(input("Enter the Number of the COURSE to Delete: "))
    if my_course_number < 1 or my_course_number > len(my_course_list):
        print("Invalid course number.\n")
    else:
        my_course = my_course_list.pop(my_course_number - 1)
        print(f"{my_course} was deleted.\n")

def main():
    course_list = ["Programming in Python",
                   "Computer Information Systems: An Overview",
                   "Business Intelligence"]

    display_menu()

    while True:
        command = input("Command: ")

        if command.lower() == "exit":
            break

        elif command.lower() == "list":
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