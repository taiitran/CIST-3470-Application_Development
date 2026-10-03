import csv

FILE_NAME = "w3_movies.csv"

def display_menu():
    print ("The Movie List program V2")
    print ("COMMAND MENU")
    print ("list - List all movies")
    print ("add - Add a movie")
    print ("del - Delete a movie")
    print ("exit - Exit the program")
    print ()

def write_movies(my_movies):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(my_movies)

def read_movies():
    my_movies = []

    with open (FILE_NAME, newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            my_movies.append(line)

    return my_movies

def list_movie(my_movie_2d_list):
    if len(my_movie_2d_list) == 0:
        print ("There are no movies in the list.\n")
    else:
        i = 1
        for my_movie in my_movie_2d_list:
            print (i, my_movie[0] + " (" + my_movie[1] + ")")
            i = i + 1
        print()

def add_movie (my_movie_2dlist):
    name = input("Name: ")
    year = input("Year: ")
    my_movie = [name, year]
    my_movie_2dlist.append(my_movie)
    write_movies(my_movie_2dlist)
    print(f"{my_movie[0]} was added.\n")

def delete_movie(my_movie_2dlist):
    movie_number = int(input("Enter the Number of the Movie to Delete: "))
    if movie_number < 1 or movie_number > len(my_movie_2dlist):
        print ("Invalid movie number.\n")
    else:
        my_movie = my_movie_2dlist.pop(movie_number - 1)
        write_movies(my_movie_2dlist)
        print(f"{my_movie[0]} was deleted.\n")

def main():
    display_menu()
    movies_2dlist = read_movies()

    while True:
        command = input("Command: ")

        if command.lower() == "exit":
            break

        if command.lower() == "list":
            list_movie(movies_2dlist)
        elif command.lower() == "add":
            add_movie(movies_2dlist)
        elif command.lower() == "del":
            delete_movie(movies_2dlist)
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
     main()
