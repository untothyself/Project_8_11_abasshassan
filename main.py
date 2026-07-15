"""
Program: Video Game Collection Manager
Author: Abass Hassan
Purpose: Main program file for the video game collection manager.
Resources: Python Materials
Date: July 2026
"""
from game import Game

games = []


def display_menu():
    """Display the program menu."""

    print("\n==============================")
    print(" Video Game Collection Manager ")
    print("==============================")
    print("1. View Games")
    print("2. Add Game")
    print("3. Remove Game")
    print("4. Exit")


def view_games():
    """Display all games."""

    if len(games) == 0:
        print("\nYour collection is empty.")

    else:

        print("\nYour Games:")

        for index, game in enumerate(games, start=1):

            print(f"{index}. {game.display()}")


def add_game():
    """Add a new game."""

    title = input("\nEnter game title: ")

    genre = input("Enter genre: ")

    rating = int(input("Enter rating (1-10): "))

    new_game = Game(title, genre, rating)

    games.append(new_game)

    print(f"{title} added successfully.")


def remove_game():
    """Remove a game."""

    if len(games) == 0:

        print("\nNo games to remove.")
        return

    view_games()

    choice = int(input("\nEnter game number: "))

    if 1 <= choice <= len(games):

        removed = games.pop(choice - 1)

        print(f"{removed.title} removed.")

    else:

        print("Invalid selection.")


def main():
    """Run the program."""

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

            print("Goodbye!")
            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()