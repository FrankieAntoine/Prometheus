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

        # Enemy Sprite definition
        self.enemySprite = None
        self.enemySpriteBackground = None

        # Battle variables
        self.playerHP = None
        self.enemyHP = None

    # Function that gets the enemy based on the players current area
    def getEnemy(self) -> Enemy:
        return self.game.enemyModule.z1Enemies[self.game.player.currentArea-1]

    # Function that sets the local values of the player and enemy using the player data and passed enemy data
    def initializeBattle(self):

        # Get an enemy from getEnemy function that uses the player's current area to determine the enemy
        self.enemy = self.getEnemy()

        # variable defaults
        self.game.page_battle.drawClicked = False
        self.game.page_battle.inspectClicked = False

        # Place enemy sprite and background
        if self.enemy.sprite != None:
            self.enemySpriteBackground = self.game.page_battle.background.create_rectangle(380, 225, 580, 400, fill="grey")
        self.enemySprite = self.game.page_battle.background.create_image(480, 325, image=self.enemy.sprite, anchor="center")

        # Initialize battle variables
        self.playerHP = self.game.player.hp
        self.enemyHP = self.enemy.hp

        # Show battle buttons
        self.game.page_battle.show_buttons()

    # Function that attacks the enemy using the players chosen attack
    def playerAttack(self):
        pass

    # Function that attacks the player using the randomly chosen enemy attack
    def enemyAttack(self):
        pass

    # Function the decides the end reult of a battle
    def endBattle(self, type):

        # Delete sprite and background from battle page
        self.game.page_battle.background.delete(self.enemySprite)
        self.game.page_battle.background.delete(self.enemySpriteBackground)

        self.game.page_battle.hide_buttons()

        # battle ended: Ran away
        if type == 3:
            print("You Successfully Ran Away!")