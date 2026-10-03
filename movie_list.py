def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

# the function prints movie number and movie name of the movies
# stores in whatever list that is passed to "my_movie_list".
def list_movie(my_movie_list):
    if len(my_movie_list) == 0:
        print("There are no movies in the list. \n")
    else:
        # A movie number is counted starting from 1.
        my_movie_number = 1
        for movie in my_movie_list:
            print(my_movie_number, movie)
            my_movie_number = my_movie_number + 1
        print()

# the function:
# 1) prompts user to enter a movie name.
# 2) adds this movie to whatever list that is passed to "my_movie_list".
def add_movie(my_movie_list):
    my_movie = input("Name: ")
    my_movie_list.append(my_movie)
    print(f"{my_movie} was added.\n")

# the function:
# 1) prompts the user to enter a movie number.
# 2) checks if the number provided is valid:
# - a movie is only valid when it's >= 1
# AND <= the count of the movies maintained by the program.
# 3) deletes the movie based on the movie number provided by the user.
# 4) prints the name of the movie deleted.
def delete_movie(my_movie_list):
    my_movie_number = int(input("Enter the Number of the Movie to Delete: "))
    # a movie number is only valid when it's >= 1 
    # AND <= the counbt of the movies maintained by the program.
    if my_movie_number < 1 or my_movie_number > len(my_movie_list):
        print("Invalid movie number.\n")
    else:
        # a movie number is counted starting from 1,
        # so the index of the movie in the list must be: movie_number - 1
        my_movie = my_movie_list.pop(my_movie_number - 1)
        print(f"{my_movie} was deleted.\n")

def main():
    movie_list = ["Monty Python and the Holy Grail",
                  "On the Waterfront",
                  "Cat on a Hot Tin Roof"]
    
    display_menu()

    while True:
        command = input("Command: ")

        if command.lower() == "exit":
            break

        if command.lower() == "list":
            list_movie(movie_list)
        elif command.lower() == "add":
            add_movie(movie_list)
        elif command.lower() == "del":
            delete_movie(movie_list)
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()

    
