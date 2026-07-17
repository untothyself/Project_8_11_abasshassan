"""
Program: Video Game Collection Manager
Author: Abass Hassan
Purpose: Unit tests for the Game classes.
Resources: Python Course Chapters 8-11
Date: July 2026
"""

import unittest

from game import Game
from game import FavoriteGame


class TestGame(unittest.TestCase):
    """Tests for the Game class."""

    def test_create_game(self):
        """Test creating a Game object."""

        game = Game("Hades", "Roguelike", 9)

        self.assertEqual(game.title, "Hades")
        self.assertEqual(game.genre, "Roguelike")
        self.assertEqual(game.rating, 9)

    def test_display(self):
        """Test the display method."""

        game = Game("Hades", "Roguelike", 9)

        self.assertEqual(
            game.display(),
            "Hades (Roguelike) - 9/10"
        )

    def test_to_dict(self):
        """Test converting a Game to a dictionary."""

        game = Game("Hades", "Roguelike", 9)

        expected = {
            "title": "Hades",
            "genre": "Roguelike",
            "rating": 9,
            "favorite": False
        }

        self.assertEqual(game.to_dict(), expected)


class TestFavoriteGame(unittest.TestCase):
    """Tests for the FavoriteGame class."""

    def test_favorite_display(self):

        game = FavoriteGame(
            "Scarlet Hollow",
            "Visual Novel",
            10
        )

        self.assertEqual(
            game.display(),
            "⭐ Scarlet Hollow (Visual Novel) - 10/10"
        )

    def test_favorite_dictionary(self):

        game = FavoriteGame(
            "Scarlet Hollow",
            "Visual Novel",
            10
        )

        expected = {
            "title": "Scarlet Hollow",
            "genre": "Visual Novel",
            "rating": 10,
            "favorite": True
        }

        self.assertEqual(game.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()