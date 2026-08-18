from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.game import Game

from game.item import Item, Items

# Generic class that defines a singular enemy
class Enemy:
    def __init__(self, name, hp, evo, item1 = None, item2 = None, sprite = None):
        self.name = name
        self.hp = hp
        self.evo = evo
        self.item1 = item1
        self.item2 = item2
        self.sprite = sprite

# A class that creates and contains all enemies in the game
class Enemies:
    def __init__(self, game: Game):
        self.game = game

        self.e_z1a1 = Enemy("Villager - Weak", 80, 1, sprite=self.game.imageModule.z1Sprites[0], item1=self.game.itemModule.spear)
        self.e_z1a4 = Enemy("Soldier - Weak", 80, 1, sprite=self.game.imageModule.z1Sprites[1])
        self.e_z1a7 = Enemy("Guardian - Weak", 80, 1, sprite=self.game.imageModule.z1Sprites[2])
        self.e_z1a10 = Enemy("Viper The Jet - BOSS", 80, 1)