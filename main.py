"""
Program: Video Game Collection Manager
Author: Abass Hassan
Purpose: Main program file for the video game collection manager.
Resources: Python Materials
Date: July 2026
"""
games = []


def display_welcome():
    """
    Display the welcome message for the program.
    """

    print("\n==============================")
    print(" Video Game Collection Manager ")
    print("==============================")
    print("1. View Game")
    print("2. Add Game")
    print("3. Remove Game")
    print("4. Exit")

def view_games():
    """
    Display all games in the collection
    """
    if len(games) == 0:
        print("\nYour collection is empty")
    else:
        print("\nYour Games:")

        for index, game in enumerate(games, start=1):
            print(f"{index}. {game}")
def add_game():
    """
    Add a new game to collection
    """
    title = input("\nEnter game title: ")

    games.append(title)

    print(f"{title} added")

def remove_game():
    """
    Remove game from collection
    """
    if len(games) == 0:
        print("\nNo games to remove.")
        return
    view_games()
    choice = int(input("\nEnter the number of games to remove: "))
    if 1 <= choice <= len(games):
        removed_game = games.pop(choice - 1)
        print (f"{removed_game} removed.")
    else: 
        print("Invalid .")
    



def main():
    """
    Run the main program.
    """
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            view_games()
        elif choice == "2":
            add_game()
        elif choice == "3":
            remove_game()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid. Try Again")
    

    


if __name__ == "__main__":
    main()