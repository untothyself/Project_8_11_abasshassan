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
    print("\n==============================")
    print(" Video Game Collection Manager ")
    print("==============================")
    print("1. View Games")
    print("2. Add Game")
    print("3. Remove Game")
    print("4. Exit")


def view_games():

    if len(games) == 0:

        print("\nNo games in collection.")

    else:

        print("\nYour Games:")

        for index, game in enumerate(games, start=1):

            print(f"{index}. {game.display()}")


def add_game():

    title = input("\nTitle: ")

    genre = input("Genre: ")

    rating = int(input("Rating: "))

    games.append(Game(title, genre, rating))

    print("Game added.")


def remove_game():

    if len(games) == 0:

        print("Collection empty.")

        return

    view_games()

    choice = int(input("\nGame number: "))

    if 1 <= choice <= len(games):

        removed = games.pop(choice - 1)

        print(f"{removed.title} removed.")

    else:

        print("Invalid choice.")


def main():

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

            print("Collection saved.")

            print("Goodbye!")

            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()