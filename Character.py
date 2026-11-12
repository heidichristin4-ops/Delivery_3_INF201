
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


class Warrior(Character):
    """
    Warrior is a defensive specialist.
    Incoming damage is reduced by armor.
    """

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon=None,
        armor: int = 5
    ) -> None:

        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        """
        Reduce incoming damage using armor before
        applying damage to HP.
        """

        reduced_damage = max(0, damage - self.armor)

        super().take_damage(reduced_damage)

class Mage(Character):
    """
    Mage uses mana to cast powerful spells.
    """

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon=None,
        mana: int = 30,
        mana_max: int = 30
    ) -> None:

        super().__init__(name, hp_max, damage, weapon)

        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """
        Cast a spell if enough mana is available.
        Otherwise perform a normal attack and
        restore some mana.
        """

        if self.mana >= 10:

            self.mana -= 10

            spell_damage = self.damage * 2

            print(
                f"{self.name} casts a spell and deals "
                f"{spell_damage} damage!"
            )

            target.take_damage(spell_damage)

        else:

            print(
                f"{self.name} does not have enough mana "
                f"and uses a normal attack."
            )

            self.mana = min(self.mana + 5, self.mana_max)

            super().attack(target)