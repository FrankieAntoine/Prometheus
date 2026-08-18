import tkinter as tk
from resources.page import Page

# Class that defines the save page in its entirety
class SavePage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_saves, game.imageModule.bg_z1a0)

        # Visual Save File representation creation

        # Save file componient definitions
        self.text_save1_title: tk.Label = None; self.text_save1_keys: tk.Message = None; self.text_save1_data: tk.Message = None; self.btn_save1: tk.Button = None
        self.text_save2_title: tk.Label = None; self.text_save2_keys: tk.Message = None; self.text_save2_data: tk.Message = None; self.btn_save2: tk.Button = None
        self.text_save3_title: tk.Label = None; self.text_save3_keys: tk.Message = None; self.text_save3_data: tk.Message = None; self.btn_save3: tk.Button = None

        # x variable storing the x value difference between each save file
        x = 240

        # For loop to create each componient dynamically
        for i in range(0, 3):
    
            # Background
            self.background.create_rectangle(150 + (i*x), 90, 330 + (i*x), 450, fill="white", outline="black", width=2)
    
            # Title
            save_lbl = tk.Label(self.frame, text="SAVE " + str(i+1), font=self.game.subtitle15, bg="grey")
            save_lbl.place(x=240 + (i*x), y=120, width=180, height=50, anchor="n")
    
            # Keys
            save_keys = tk.Message(self.frame, text=self.game.getListStr(self.game.player.keys, 1), font=self.game.body13, bg="white", anchor="nw", justify="left")
            save_keys.place(x=150 + (i*x), y=170, width=90, height=230)
    
            # Data
            save_data = tk.Message(self.frame, text=self.game.getListStr(self.game.saveModule.savesData[i], 0), font=self.game.body13, bg="white", anchor="ne", justify="right")
            save_data.place(x=240 + (i*x), y=170, width=90, height=230)
    
            # Button
            save_button = tk.Button(self.frame, text="LOAD", font=self.game.body13, bg="white", command=lambda save=i + 1: self.loadGame(save))
            save_button.place(x=240 + (i*x), y=400, width=180, height=50, anchor="n")
    
            # transfer the dynamically created componients back into their repective save file names
            if i == 0: self.text_save1_title, self.text_save1_keys, self.text_save1_data, self.btn_save1 = save_lbl, save_keys, save_data, save_button
            elif i == 1: self.text_save2_title, self.text_save2_keys, self.text_save2_data, self.btn_save2 = save_lbl, save_keys, save_data, save_button
            elif i == 2: self.text_save3_title, self.text_save3_keys, self.text_save3_data, self.btn_save3 = save_lbl, save_keys, save_data, save_button

    # Function that loads the player and goes to the main page
    def loadGame(self, saveNumber):
        print("Save" + str(saveNumber) + " Loaded!")
        self.game.saveModule.loadPlayer(saveNumber)
        self.game.changePage(self.game.page_main)

    # No update needed
    def update(self):
        pass