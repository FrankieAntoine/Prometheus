import tkinter as tk
from resources.page import Page

# Class that defines the battle page in its entirety
class BattlePage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_battle, game.imageModule.z1Backgrounds[0])

        self.drawClicked = False
        self.inspectClicked = False

        # Enemy title
        self.lbl_enemyTitle = tk.Label(self.frame, text="Enemy Title", anchor="center", font=self.game.title25, bg="white", fg="green", highlightbackground="grey", highlightthickness=7)
        self.lbl_enemyTitle.place(x=480, y=25, width=960, height=70, anchor="n")

        # Battle Menu
        self.background.create_rectangle(0, 400, 960, 540, fill="white", outline="grey", width=2)

        # Battle menu buttons

        # Items
        self.btn_items = tk.Button(self.frame, text="ITEMS", font=self.game.body13, bg="yellow", activebackground="black", activeforeground="white", command=self.command_items)

        # Draw / Attack
        self.btn_draw = tk.Button(self.frame, text="DRAW", font=self.game.body13, bg="red", activebackground="black", activeforeground="white", command=self.command_draw)
        self.btn_attack = tk.Button(self.frame, text="ATTACK", font=self.game.body13, bg="red", activebackground="black", activeforeground="white", command=self.command_attack)

        # Inspect / Talk
        self.btn_inspect = tk.Button(self.frame, text="INSPECT", font=self.game.body13, bg="green", activebackground="black", activeforeground="white", command=self.command_inspect)
        self.btn_talk = tk.Button(self.frame, text="NEGOTIATE", font=self.game.body13, bg="green", activebackground="black", activeforeground="white", command=self.command_talk)

        # Run
        self.btn_run = tk.Button(self.frame, text="RUN", font=self.game.body13, bg="blue", activebackground="black", activeforeground="white", command=self.command_run)
    
    def command_items(self):
        self.hide_buttons()
        self.game.after(2000, self.show_buttons)

    def command_draw(self):
        self.drawClicked = True
        self.hide_buttons()
        self.game.after(2000, self.show_buttons)

    def command_attack(self):
        self.hide_buttons()
        self.game.after(2000, self.show_buttons)

    def command_inspect(self):
        self.inspectClicked = True
        self.hide_buttons()
        self.game.after(2000, self.show_buttons)

    def command_talk(self):
        self.hide_buttons()
        self.game.after(2000, self.show_buttons)

    def command_run(self):
        self.hide_buttons()
        self.game.battleModule.endBattle(3)
        self.game.changePage(self.game.page_main)

    def show_buttons(self):
        self.btn_items.place(x=240, y=470, width=100, height=80, anchor="center")

        if self.drawClicked:
            self.btn_attack.place(x=400, y=470, width=100, height=80, anchor="center")
        else:
            self.btn_draw.place(x=400, y=470, width=100, height=80, anchor="center")
        if self.inspectClicked:
            self.btn_talk.place(x=560, y=470, width=100, height=80, anchor="center")
        else:
            self.btn_inspect.place(x=560, y=470, width=100, height=80, anchor="center")
        self.btn_run.place(x=720, y=470, width=100, height=80, anchor="center")

    def hide_buttons(self):
        self.btn_items.place_forget()
        self.btn_draw.place_forget()
        self.btn_attack.place_forget()
        self.btn_inspect.place_forget()
        self.btn_talk.place_forget()
        self.btn_run.place_forget()

    def update(self):

        # Background change
        if self.game.player.currentArea == 10:
            self.changeBackgroundImage(self.game.imageModule.bg_z1b1)
        else:
            self.changeBackgroundImage(self.game.imageModule.z1Backgrounds[self.game.player.currentArea-1])

        # Update enemy title
        self.lbl_enemyTitle.config(text=self.game.battleModule.enemy.name + "  " + str(self.game.battleModule.enemyHP) + "/" + str(self.game.battleModule.enemy.hp) + " HP")

        # Button placement
        self.show_buttons()