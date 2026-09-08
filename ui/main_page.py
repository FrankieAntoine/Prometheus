import tkinter as tk
from resources.page import Page

# Class that defines the main page in its entirety
class MainPage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_main, game.imageModule.z1Backgrounds[0])

        # List of all of the area names
        self.areaNames = [
            "Tutario", "The Forest", "The Dark Oak", 
            "The Cavern Enterance", "The Deep Dark",
            "The Volcanic Core", "The Cavern Exit", 
            "The Great Bridge", "The Peak of The Mountain", 
            "Final Destination"
        ]

        # Start menu title
        self.lbl_area = tk.Label(self.frame, anchor="center", font=self.game.title25, bg="white", fg="green", highlightbackground="grey", highlightthickness=7)
        self.lbl_area.place(x=480, y=25, width=960, height=70, anchor="n")

        # Button Creation
        self.btn_nextArea = tk.Button(self.frame, text="Next Area    --->", anchor="e", font=("Consolas", 10, "bold"), bg="white", command=self.nextArea)
        self.btn_prevArea = tk.Button(self.frame, text="<---    Prev Area", anchor="w",font=("Consolas", 10, "bold"), bg="white", command=self.prevArea) 

        # Battle Button
        self.btn_battle = tk.Button(self.frame, text="Battle", anchor="center",font=self.game.title25, bg="white", fg="black", command=self.battle, activebackground="red") 
        self.btn_battle.place(x=480, y=500, width=180, height=65, anchor="s")

        # Inventory Button
        self.btn_inv = tk.Button(self.frame, text="Inventory", anchor="center",font=self.game.subtitle15, bg="white", fg="black", command=self.inventory, activebackground="green") 
        self.btn_inv.place(x=600, y=500, width=120, height=50, anchor="w")

    # A function that goes to the next area if possible
    def nextArea(self):
        global player
        self.game.player.currentArea = self.game.player.currentArea + 1
        self.update()

    # A function that goes to the previous area if possible
    def prevArea(self):
        global player
        self.game.player.currentArea = self.game.player.currentArea - 1
        self.update()

    # A function that goes to the battle sequence for the current area
    def battle(self):
        
        # Initialize battle
        self.game.battleModule.initializeBattle()
        
        # Change page
        self.game.changePage(self.game.page_battle)

    # Function that goes to the inventory page
    def inventory(self):
        self.game.changePage(self.game.page_inventory)

    # Function that completely updates all objects within page main. This incudes next and prev area buttons amd the title of area
    def update(self):
        self.changeBackgroundImage(self.game.imageModule.z1Backgrounds[self.game.player.currentArea-1])
        self.lbl_area.config(text=self.areaNames[self.game.player.currentArea-1])
        self.btn_prevArea.place_forget()
        self.btn_nextArea.place_forget()
        self.btn_nextArea.place(x=960, y=32, width=180, height=56, anchor="ne")
        self.btn_prevArea.place(x=0, y=32, width=180, height=56, anchor="nw")
        if self.game.player.currentArea == 1:
            self.btn_prevArea.place_forget()
        if (self.game.player.currentArea == self.game.player.area) or (self.game.player.currentArea == 10):
            self.btn_nextArea.place_forget()

    # Function that deals with keyboard presses
    def on_key_press(self, event):
        pass

    # Function that deals with keyboard releases
    def on_key_release(self, event):
        pass