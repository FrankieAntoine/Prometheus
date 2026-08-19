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
        self.z1Enemies = []

        self.e_z1a1 = Enemy("Promethian Villager", 80, 1, sprite=self.game.imageModule.z1Sprites[0], item1=self.game.itemModule.spear); self.z1Enemies.append(self.e_z1a1) # Weak
        self.e_z1a2 = Enemy("Promethian Villager", 100, 1, sprite=self.game.imageModule.z1Sprites[0], item1=self.game.itemModule.spear); self.z1Enemies.append(self.e_z1a2) # Normal
        self.e_z1a3 = Enemy("Promethian Villager", 120, 1, sprite=self.game.imageModule.z1Sprites[0], item1=self.game.itemModule.spear); self.z1Enemies.append(self.e_z1a3) # Strong
        self.e_z1a4 = Enemy("Promethian Soldier", 180, 2, sprite=self.game.imageModule.z1Sprites[1]); self.z1Enemies.append(self.e_z1a4) # Weak
        self.e_z1a5 = Enemy("Promethian Soldier", 215, 2, sprite=self.game.imageModule.z1Sprites[1]); self.z1Enemies.append(self.e_z1a5) # Normal
        self.e_z1a6 = Enemy("Promethian Soldier", 250, 2, sprite=self.game.imageModule.z1Sprites[1]); self.z1Enemies.append(self.e_z1a6) # Strong
        self.e_z1a7 = Enemy("Promethian Guardian", 310, 3, sprite=self.game.imageModule.z1Sprites[2]); self.z1Enemies.append(self.e_z1a7) # Weak
        self.e_z1a8 = Enemy("Promethian Guardian", 355, 3, sprite=self.game.imageModule.z1Sprites[2]); self.z1Enemies.append(self.e_z1a8) # Normal
        self.e_z1a9 = Enemy("Promethian Guardian", 390, 3, sprite=self.game.imageModule.z1Sprites[2]); self.z1Enemies.append(self.e_z1a9) # Strong
        self.e_z1a10 = Enemy("Viper The Jet", 2000, 4); self.z1Enemies.append(self.e_z1a10) # BOSS