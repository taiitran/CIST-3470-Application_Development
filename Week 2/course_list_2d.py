def display_menu():
    print("The course List program V2")
    print("COMMAND MENU")
    print("list - List all courses")
    print("add - Add a course")
    print("del - Delete a course")
    print("exit - Exit program")
    print()

def list_course(my_course_2dlist):
    if len(my_course_2dlist) == 0:
        print("There are no courses in the list.\n")
    else:
        my_course_number = 1
        for course in my_course_2dlist:
            print(my_course_number, course[0], course[1] + " (" + str(course[2]) + ")")
            my_course_number = my_course_number + 1
        print()

def add_course(my_course_2dlist):
    number = input("Course number: ")
    name = input("Course name: ")
    credit = input("Credits: ")
    my_course = [number, name, credit]
    my_course_2dlist.append(my_course)
    print(f"{my_course[1]} was added.\n")

def delete_course(my_course_2dlist):
    my_course_number = int(input("Enter Course No. to Delete: "))
    if my_course_number < 1 or my_course_number > len(my_course_2dlist):
        print("Invalid course number.\n")
    else:
        my_course = my_course_2dlist.pop(my_course_number - 1)
        print(f"{my_course[1]} was deleted.\n")

def main():
    course_list = [["CIST 3470","Programming in Python", "4"],
                   ["CIST 2010","Computer Information Systems: An Overview", "4"],
                   ["CIST 3450","Business Intelligence", "4"]]

    display_menu()

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


