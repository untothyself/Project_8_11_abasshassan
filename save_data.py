"""
Program: Video Game Collection Manager
Author: Abass Hassan
Purpose: Save and load game data.
Resources: Python Course Chapters
Date: July 2026
"""

import json
from game import Game


def save_games(games):
    """Save all games to games.json."""

    data = []

    for game in games:
        data.append(game.to_dict())

    with open("games.json", "w") as file:
        json.dump(data, file, indent=4)


def load_games():
    """Load games from games.json."""

    games = []

    try:

        with open("games.json", "r") as file:

            data = json.load(file)

            for item in data:
                games.append(
                    Game(
                        item["title"],
                        item["genre"],
                        item["rating"]
                    )
                )

    except FileNotFoundError:
        print("No saved collection found. Start a new collection")
    except json.JSONDecodeError:
        print("Saved data is corrupt. start new collection.")

    return games