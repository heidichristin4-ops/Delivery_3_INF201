
class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicates protected attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon # Optional weapon attribute

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        
        target.take_damage(damage)

    # ADDED, Method to reduce the character HP
    def take_damage(self, damage: int) -> None:
        """Reduce the character's HP"""
        self._hp -= damage
        self._hp = max(self._hp, 0)

    # ADDED, Method to restore the character's HP
    def heal(self, amount: int) -> None:
        """Restore the character's HP"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    # ADDED, Read only property to check if the character is alive
    @property
    def is_alive(self) -> bool:
        """Check if the character is alive"""
        return self._hp > 0

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
