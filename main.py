"""
Program: Video Game Collection Manager
Author: Abass Hassan
Purpose: Main program file for the video game collection manager.
Resources: Python Materials
Date: July 2026
"""
from game import Game
from save_data import save_games, load_games

games = load_games()


def display_menu():
    """Display the menu."""
    print("\n==============================")
    print(" Video Game Collection Manager ")
    print("==============================")
    print("1. View Games")
    print("2. Add Game")
    print("3. Remove Game")
    print("4. Exit")


def view_games():
    """Display all games"""
    if len(games) == 0:

        print("\nNo games in collection.")

    else:

        print("\nYour Games:")

        for index, game in enumerate(games, start=1):

            print(f"{index}. {game.display()}")


def add_game():
    """Add new game"""
    title = input("\nTitle: ")

    genre = input("Genre: ")

    while True:
        try:
            rating = int(input("rating (1-10): "))
            if 1 <= rating <= 10:
                break
            print("Rating has to be between 1 and 10")

        except ValueError:
            print("Please enter a whole number.")


    games.append(Game(title, genre, rating))

    print("Game added.")


def remove_game():
    """Remove a game."""
    if len(games) == 0:

        print("Collection empty.")

        return

    view_games()

    try:
        choice = int(input("\nGame number: "))

        if 1 <= choice <= len(games):

            removed = games.pop(choice - 1)

            print(f"{removed.title} removed.")

        else:

            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """run the program"""
    while True:

        display_menu()

        choice = input("\nChoose: ")

        if choice == "1":

            view_games()

        elif choice == "2":

            add_game()

        elif choice == "3":

            remove_game()

        elif choice == "4":

            save_games(games)

            print("\nCollection saved.")

            print("Goodbye!")

            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()