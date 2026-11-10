
import random  # Import random to generate random numbers


class Dice:
    """Represents a dice with a given number of sides"""

    # Dice class
    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides (default = 6)
        """
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")

        self.sides = sides

    # function for rolling the dice
    def roll(self) -> int:
        """Roll the dice and return a random number"""
        return random.randint(1, self.sides)

    # Representation of dice object
    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides={self.sides})"

    # Allowing the dice to be called like a function
    def __call__(self) -> int:
        """Roll the dice when the object is called"""
        return self.roll()
