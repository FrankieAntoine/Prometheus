from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.game import Game

import tkinter as tk
from game.enemy import Enemy

# Class that does everything to do with a battle
class BattleManager:
    def __init__(self, game):
        self.game: Game = game
        self.enemy: Enemy = None

        self.enemySprite = None

    # Function that gets the enemy based on the players current area
    def getEnemy(self) -> Enemy:
        if self.game.player.currentArea <= 3:
            return self.game.enemyModule.e_z1a1
        elif self.game.player.currentArea <= 6:
            return self.game.enemyModule.e_z1a4
        elif self.game.player.currentArea <= 9:
            return self.game.enemyModule.e_z1a7
        else:
            return self.game.enemyModule.e_z1a10

    # Function that sets the local values of the player and enemy using the player data and passed enemy data
    def initializeBattle(self):

        self.enemy = self.getEnemy()

        # variable defaults
        self.drawClicked = False
        self.inspectClicked = False

        # Place enemy sprite
        self.enemySprite = self.game.page_battle.background.create_image(480, 325, image=self.enemy.sprite, anchor="center")

    # Function that attacks the enemy using the players chosen attack
    def playerAttack(self):
        pass

    # Function that attacks the player using the randomly chosen enemy attack
    def enemyAttack(self):
        pass

    # Function the decides the end reult of a battle
    def endBattle(self):
        pass