"""
Program: Video Game Collection Manager
Author: Abass Hassan
Purpose: Defines the Game class.
Resources: Python class Materials
Date: July 2026
"""


class Game:
    """Represents one video game."""

    def __init__(self, title, genre, rating):
        """Create a new Game object."""

        self.title = title
        self.genre = genre
        self.rating = rating

    def display(self):
        """Return a description of the game."""

        return f"{self.title} ({self.genre}) - {self.rating}/10"
    
    def to_dict(self):
        "Turn game object into a dictionary"

        return {
            "title": self.title,
            "genre": self.genre,
            "rating": self.rating
        }