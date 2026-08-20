import tkinter as tk
from resources.page import Page

# Class that defines the battle page in its entirety
class BattlePage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_battle, game.imageModule.z1Backgrounds[0])

        self.drawClicked = False
        self.inspectClicked = False

        self.spacebarPressed = False

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
        self.game.after(500, self.show_buttons)

    def command_draw(self):
        self.drawClicked = True
        self.hide_buttons()
        self.game.after(500, self.show_buttons)

    def command_attack(self):
        self.hide_buttons()
        self.attackSequence()

    def command_inspect(self):
        self.inspectClicked = True
        self.hide_buttons()
        self.game.after(500, self.show_buttons)

    def command_talk(self):
        self.hide_buttons()
        self.game.after(500, self.show_buttons)

    def command_run(self):
        self.hide_buttons()
        self.game.battleModule.endBattle(3)
        self.game.changePage(self.game.page_main)

    # Function that dhoes the battle buttons based on if the draw or inspect buttons have already been pressed
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

    # Function that removes all of the battle buttons
    def hide_buttons(self):
        self.btn_items.place_forget()
        self.btn_draw.place_forget()
        self.btn_attack.place_forget()
        self.btn_inspect.place_forget()
        self.btn_talk.place_forget()
        self.btn_run.place_forget()

    # Function that creates the attack UI and starts the attack animation
    def attackSequence(self):

        # Create battle UI
        self.damageModifier = self.background.create_image(480, 470, image=self.game.imageModule.damageModifier, anchor="center")
        self.playerRect = self.background.create_rectangle(100, 420, 118, 520, fill="grey", outline="black", width=7)

        # Start animation
        self.game.after(500, lambda: self.attackAnimation())

    # Recursive function that moves the player rect until a spacebar input stops it
    def attackAnimation(self, xOffset=0):

        # Stop at 735 pixels from starting position
        if xOffset >= 735:
            self.spacebarPressed = True

        # Offset the player rect by 10 pixels
        xOffset += 10
        self.background.move(self.playerRect, 10, 0)

        # If spacebar not clicked, recall function every 15ms
        if not self.spacebarPressed:
            self.game.after(15, lambda: self.attackAnimation(xOffset))

        # If spacebar clicked, set it back to false and detete the battle UI
        else:
            self.spacebarPressed = False
            self.game.after(500, lambda: self.background.delete(self.damageModifier))
            self.game.after(500, lambda: self.background.delete(self.playerRect))
            self.game.after(500, self.show_buttons)

    # Update function that is usually called once at the begining of a page switch or major page changes
    def update(self):

        # Background change
        if self.game.player.currentArea == 10:
            self.changeBackgroundImage(self.game.imageModule.bg_z1b1)
        else:
            self.changeBackgroundImage(self.game.imageModule.z1Backgrounds[self.game.player.currentArea-1])

        # Update enemy title
        self.lbl_enemyTitle.config(text=self.game.battleModule.enemy.name + "  " + str(self.game.battleModule.enemyHP) + "/" + str(self.game.battleModule.enemy.hp) + " HP")

    # Function that deals with keyboard presses
    def on_key_press(self, event):
        if event.keysym == "space":
            self.spacebarPressed = True

    # Function that deals with keyboard releases
    def on_key_release(self, event):
        pass