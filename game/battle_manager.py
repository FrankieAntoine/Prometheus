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

        # Variable for player damage modifier based on attack sequence
        self.playerDamageModifier = 0

    # Function that gets the enemy based on the players current area
    def getEnemy(self) -> Enemy:
        return self.game.enemyModule.z1Enemies[self.game.player.currentArea-1]

    def setModifier(self, xCenterValue: int):
        print(xCenterValue) # for testing
 
        if xCenterValue <= 150 or 810 <= xCenterValue:
            print("MISS!")
            self.playerDamageModifier = 0
        elif xCenterValue <= 260 or 700 <= xCenterValue:
            print("REALLY BAD")
            self.playerDamageModifier = 0.25
        elif xCenterValue <= 370 or 590 <= xCenterValue:
            print("BAD")
            self.playerDamageModifier = 0.5
        elif xCenterValue <= 430 or 530 <= xCenterValue:
            print("OKAY")
            self.playerDamageModifier = 1
        elif xCenterValue <= 465 or 495 <= xCenterValue:
            print("GOOD")
            self.playerDamageModifier = 1.15
        elif xCenterValue == 480:
            print("PERFECT!!!")
            self.playerDamageModifier = 2
        elif 465 <= xCenterValue <= 495:
            print("EXCELLENT!")
            self.playerDamageModifier = 1.5
        else:
            print("ERR")
            self.playerDamageModifier = 0

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
        self.game.page_battle.show_battleButtons()

    # Function that attacks the enemy using the players chosen attack
    def playerAttack(self, chosenItem):
        self.game.page_battle.hide_attackOptions()
        self.game.page_battle.attackSequence(chosenItem)

    # Function that calculates the damge done to the enemy and sets the new values
    def calculatePlayerDamage(self, chosenItem):
        playerDamage = chosenItem.pointValue * self.playerDamageModifier
        print("You Dealt", str(playerDamage), "Damage! (" + str(self.playerDamageModifier) + "x)\n")
        self.enemyHP -= playerDamage
        if self.enemyHP <= 0:
            self.enemyHP = 0
            self.game.after(750, lambda: self.endBattle(1))
        else:
            self.game.after(500, self.game.page_battle.show_battleButtons)

    # Function that attacks the player using the randomly chosen enemy attack
    def enemyAttack(self):
        pass

    # Function the decides the end reult of a battle
    def endBattle(self, type):

        # Delete sprite and background from battle page
        self.game.page_battle.background.delete(self.enemySprite)
        self.game.page_battle.background.delete(self.enemySpriteBackground)

        self.game.page_battle.hide_battleButtons()

        # battle ended: Player Won
        if type == 1:
            print("You Won!")
            self.game.after(500, self.game.changePage(self.game.page_main))

        # battle ended: Ran Away
        elif type == 3:
            print("You Successfully Ran Away!")