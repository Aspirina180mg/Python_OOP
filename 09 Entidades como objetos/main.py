"""crea un jugador y un enemigo, luego los hace luchar"""
from character import Player, Enemy

player = Player("Hero", 100, 0)
enemy = Enemy("Goblin", 30, 10)

enemy.attack(player)
player.gain_experience(50)
