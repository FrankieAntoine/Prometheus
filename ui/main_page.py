import tkinter as tk
from ui.page import Page

# Class that defines the start menu in its entirety
class MainPage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_main, game.images.z1Backgrounds[0])

        # Button Creation
        self.btn_nextArea = tk.Button(self.frame, text="Next Area", font=("Consolas", 10, "bold"), bg="white", anchor="center", command=self.command_nextArea)
        self.btn_prevArea = tk.Button(self.frame, text="Prev Area", font=("Consolas", 10, "bold"), bg="white", anchor="center", command=self.command_prevArea) 

    def update(self):
        self.changeBackgroundImage(self.game.images.z1Backgrounds[self.game.player.currentArea-1])
        self.btn_prevArea.place_forget()
        self.btn_nextArea.place_forget()
        self.btn_nextArea.place(x=960, y=540, width=180, height=50, anchor="se")
        self.btn_prevArea.place(x=0, y=540, width=180, height=50, anchor="sw")
        if self.game.player.currentArea == 1:
            self.btn_prevArea.place_forget()
        if (self.game.player.currentArea == self.game.player.area) or (self.game.player.currentArea == 10):
            self.btn_nextArea.place_forget()

    # A function that goes to the next area if possible
    def command_nextArea(self):
        global player
        self.game.player.currentArea = self.game.player.currentArea + 1
        self.update()

    # A function that goes to the previous area if possible
    def command_prevArea(self):
        global player
        self.game.player.currentArea = self.game.player.currentArea - 1
        self.update()