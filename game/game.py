import tkinter as tk

# Game Modules
from game.player import Player
from game.item import Items
from resources.fonts import load_fonts
from resources.images import Images
from game.enemy import Enemies
from game.save_manager import SaveManger
from game.battle_manager import BattleManager

# Pages
from resources.page import Page
from ui.start_page import StartPage
from ui.save_page import SavePage
from ui.main_page import MainPage
from ui.battle_page import BattlePage

# Class that runs the main operations and variables of the game
class Game(tk.Tk):

    # Constructor
    def __init__(self):
        super().__init__()

        # Fonts
        load_fonts()
        self.body13 = ("Consolas", 13, "bold")
        self.subtitle15 = ("Consolas", 15, "bold")
        self.title25 = ("Lucida Unicode Calligraphy", 25, "bold")

        # Window Configuration
        self.geometry("960x540")
        self.resizable(False, False)
        self.title("Prometheus")

        # Keyboard input initialization
        self.bind("<KeyPress>", self.on_key_press_main)
        self.bind("<KeyRelease>", self.on_key_release_main)

        self.bind("<Escape>", lambda: self.destroy())

        # Game Data
        self.player = Player()
        self.itemModule = Items(self)
        self.imageModule = Images()
        self.enemyModule = Enemies(self)
        self.saveModule = SaveManger(self)
        self.battleModule = BattleManager(self)

        # Page Setup
        self.frame_start = tk.Frame(self)
        self.frame_saves = tk.Frame(self)
        self.frame_main = tk.Frame(self)
        self.frame_battle = tk.Frame(self)

        self.frames = [self.frame_start, self.frame_saves, self.frame_main, self.frame_battle]
        for frame in self.frames:
            frame.grid(row=0, column=0, sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Page Creation
        self.page_start = StartPage(self)
        self.page_saves = SavePage(self)
        self.page_main = MainPage(self)
        self.page_battle = BattlePage(self)

        # Current page function used mostly for key pressing and releasing handling between different pages
        self.currentPage: Page = None

        # Start on start page
        self.changePage(self.page_start)

    # Change page funtion
    def changePage(self, page):
        self.currentPage = page
        page.update()
        page.lift()

    # A function to turn the save data lists into a string for the save files to show
    def getListStr(self, data, type):
        dataStr = ""
        for i in range(len(data) - 2):
            if type == 0:
                dataStr+= str(data[i]) + "\n"
            elif type == 1:
                dataStr+= str(data[i]).capitalize() + ":" + "\n"
        return dataStr

    # Function that directs the key press event to the right page depending on the current page
    def on_key_press_main(self, event):
        self.currentPage.on_key_press(event)

    # Function that directs the key release event to the right page depending on the current page
    def on_key_release_main(self, event):
        self.currentPage.on_key_release(event)