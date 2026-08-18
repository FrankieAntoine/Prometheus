import tkinter as tk
from resources.page import Page

# Class that defines the start menu in its entirety
class StartPage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_start, game.imageModule.bg_z1a0)

        # Start menu title
        self.lbl_title = tk.Label(self.frame, anchor="center", text="PROMETHEUS", font=self.game.title25, bg="white", fg="green", highlightbackground="grey", highlightthickness=7)
        self.lbl_title.place(x=480, y=25, width=960, height=70, anchor="n")

        # Start button
        self.btn_start = tk.Button(self.frame, anchor="center", text="START", font=self.game.subtitle15, bg="white", fg="green", command=self.command_start)
        self.btn_start.place(x=480, y=520, width=125, height=75, anchor="s")

    # Start button command
    def command_start(self):
        self.game.changePage(self.game.page_saves)

    # No update needed
    def update(self):
        pass
        