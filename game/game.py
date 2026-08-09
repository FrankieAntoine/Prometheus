import tkinter as tk

from resources.images import Images

# Class that runs the main operations and variables of the game
class Game(tk.Tk):

    # Constructor
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.geometry("960x540")
        self.resizable(False, False)
        self.title("Prometheus")

        # Game Data
        self.player = None

