import tkinter as tk
from ui.page import Page

# Class that defines the start menu in its entirety
class StartPage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_start, game.images.bg_z1a0)

        # Start button
        btn_start = tk.Button(self.frame, anchor="center", text="START", font=("Consolas", 20, "bold"), bg="white", fg="red", command=self.command_start)
        btn_start.place(x=480, y=520, width=125, height=100, anchor="s")

    # Start button command
    def command_start(self):
        self.game.changePage(self.game.page_saves)
        