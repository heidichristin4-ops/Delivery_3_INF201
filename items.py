
from Dice import Dice # Import the dice function from Dice.py


class Weapon:
    """Represents a weapon that can be used by a character"""

    #Weapon class
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice used to calculate damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    #calculate weapon damage
    def roll_damage(self) -> int:
        """Roll the damage dice and return the result"""
        return self.damage_dice.roll()

