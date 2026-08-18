import tkinter as tk
from game.enemy import Enemy

# Class that does everything to do with a battle
class BattleManager:
    def __init__(self, game):
        self.game = game

    # Function that sets the local values of the player and enemy using the player data and passed enemy data
    def initializeBattle(self, enemy: Enemy):
        pass

    # Function that attacks the enemy using the players chosen attack
    def playerAttack(self):
        pass

    # Function that attacks the player using the randomly chosen enemy attack
    def enemyAttack(self):
        pass

    # Function the decides the end reult of a battle
    def endBattle(self):
        pass