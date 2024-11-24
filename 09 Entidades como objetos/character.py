"""se pueden llamar Player o Enemy para crear personajes
    """
class Character:
    """clase personaje base."""
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        """disminuye la vida del personaje

        Args:
            amount int: cantidad de puntos en que disminuye
        """
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        """al perder todos sus puntos de vida, el personaje muere
        """
        print(f"{self.name} has died.")


class Player(Character):
    """personaje jugable, gana experiencia"""
    def __init__(self, name, health, experience):
        super().__init__(name, health)
        self.experience = experience

    def gain_experience(self, points):
        """método para ganar experiencia"""
        self.experience += points
        print(f"{self.name} gained {points} experience points.")


class Enemy(Character):
    """clase de enemigo, hace daño al personaj jugable"""
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self, player):
        """hace daño al personaje jugable

        Args:
            player (Player): elige al jugador al que hará daño
        """
        print(f"{self.name} attacks {player.name} for {self.strength} damage")
        player.take_damage(self.strength)
