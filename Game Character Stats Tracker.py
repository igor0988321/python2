class GameCharacter:
    def __init__(self, name):
        self._name = str(name)
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        """Read-only property for the character's name."""
        return self._name

    @property
    def health(self):
        """Getter for the health attribute."""
        return self._health

    @health.setter
    def health(self, value):
        """Setter for health: prevents it from going below 0 or above 100."""
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        """Getter for the mana attribute."""
        return self._mana

    @mana.setter
    def mana(self, value):
        """Setter for mana: prevents it from going below 0 or above 50."""
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        """Getter for the level attribute."""
        return self._level

    def level_up(self):
        """Increases level and resets health and mana using their respective setters."""
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        """Returns the formatted character stats string."""
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Mana: {self.mana}")


# --- Example of usage ---
if __name__ == "__main__":
    hero = GameCharacter('Kratos')
    print(hero)

    print("\n--- Taking Damage & Using Mana ---")
    hero.health -= 30
    hero.mana -= 10
    print(hero)

    print("\n--- Leveling Up ---")
    hero.level_up()
    print(hero)