
class Battle:
    """
    Controls a battle between two characters.
    """

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        """
        One combat round:
        Hero attacks first.
        Enemy attacks if still alive.
        """

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        """
        Continue fighting until one character dies.
        """

        round_number = 1

        while self.hero.is_alive and self.enemy.is_alive:

            print(f"\nROUND {round_number}: ")

            self.play_round()

            print(
                f"{self.hero.name}: {self.hero.hp} HP"
            )
            print(
                f"{self.enemy.name}: {self.enemy.hp} HP"
            )

            round_number += 1

        if self.hero.is_alive:
            print(f"\n{self.hero.name} wins the battle!")
        else:
            print(f"\n{self.enemy.name} wins the battle!")