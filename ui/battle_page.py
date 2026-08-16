import tkinter as tk
from resources.page import Page

# Class that defines the battle page in its entirety
class BattlePage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_battle, game.images.z1Backgrounds[0])

    def update(self):
        if self.game.player.currentArea == 10:
            self.changeBackgroundImage(self.game.images.bg_z1b1)
        else:
            self.changeBackgroundImage(self.game.images.z1Backgrounds[self.game.player.currentArea-1])