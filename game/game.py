import tkinter as tk

from game.player import Player
from resources.images import Images
from game.save_manager import SaveManger

from ui.start_page import StartPage
from ui.save_page import SavePage
from ui.main_page import MainPage

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
        self.player = Player()
        self.images = Images()
        self.save_manager = SaveManger(self)

        # Page Setup

        # Frame Creation
        self.frame_start = tk.Frame(self)
        self.frame_saves = tk.Frame(self)
        self.frame_main = tk.Frame(self)

        self.frames = [self.frame_start, self.frame_saves, self.frame_main]
        for frame in self.frames:
            frame.grid(row=0, column=0, sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Page Creation
        self.page_start = StartPage(self)
        self.page_saves = SavePage(self)
        self.page_main = MainPage(self)

        # Start on start page
        self.changePage(self.page_start)

    # Change page funtion
    def changePage(self, page):
        page.lift()

    # A function to turn the save data lists into a string for the save files to show
    def getListStr(self, data, type):
        dataStr = ""
        for i in range(len(data)):
            if type == 0:
                dataStr+= str(data[i]) + "\n"
            elif type == 1:
                dataStr+= str(data[i]).capitalize() + ":" + "\n"
        return dataStr

