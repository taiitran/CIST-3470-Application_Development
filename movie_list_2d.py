def display_menu():
    print("The Movie List program V2")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

# the function prints movie number number, movie name, and release year of the movies
# stores in whatever list that is passed to "my_movie_2dlist"
def list_movie(my_movie_2dlist):
    if len (my_movie_2dlist) == 0:
        print("There are no movies in the list. \n")
    else: 
        # A movie number is counted starting from 1.
        my_movie_number = 1
        for movie in my_movie_2dlist:
            print (my_movie_number, movie[0] + " (" + str(movie[1]) + ")")
            my_movie_number = my_movie_number + 1
        print()


# the function:
# 1) prompts user to enter a movie by entering a movie name and the release year of the movie
# 2) adds this movie to whatever list that is passed to "my_movie_2dlist".
def add_movie(my_movie_2dlist):
    name = input("Name: ")
    year = input("Year: ")
    my_movie = [name, year]
    my_movie_2dlist.append(my_movie)
    print(f"{my_movie[0]} was added.\n")

# the function:
# 1) prompts the user to enter a movie number.
# 2) checks if the number provided is valid:
# - a movie is only valid when it's >= 1
# AND <= the count of the movies maintained by the program.
# 3_ deletes the movie based on the movie number provided by the user.
# 4) prints the name of the movie deleted.
def delete_movie(my_movie_2dlist):
    my_movie_number = int(input("Enter the Number of the Movie to Delete: "))
    if my_movie_number < 1 or my_movie_number > len(my_movie_2dlist):
        print("Invalid movie number.\n")
    else: 
        my_movie = my_movie_2dlist.pop(my_movie_number - 1)
        print(f"{my_movie[0]} was deleted.\n")

def main():
    movies = [["Monty Python and the Holy Grail", 1975],
               ["On the Waterfront", 1954],
               ["Cat on a Hot Tin Roof", 1958]]

    display_menu()

    while True:
        command = input("Command: ")

        if command.lower() == "exit":
            break

        if command.lower() == "list":
            list_movie(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")


if __name__ == "__main__":
    main()

               

