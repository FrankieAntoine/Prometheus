import tkinter as tk
from resources.page import Page

# Class that defines the battle page in its entirety
class BattlePage(Page):

    def __init__(self, game):
        super().__init__(game, game.frame_battle, game.imageModule.z1Backgrounds[0])

        self.drawClicked = False
        self.inspectClicked = False

        self.spacebarPressed = False

        self.animationActive = False

        # Enemy title
        self.lbl_enemyTitle = tk.Label(self.frame, text="Enemy Title", anchor="center", font=self.game.title25, bg="white", fg="green", highlightbackground="grey", highlightthickness=7)
        self.lbl_enemyTitle.place(x=480, y=25, width=960, height=70, anchor="n")

        # Battle Menu
        self.background.create_rectangle(0, 400, 960, 540, fill="white", outline="grey", width=2)

        # -----Battle menu buttons-----

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

        # -----Player attack option buttons-----

        # Player equipped 1
        self.btn_attack1 = tk.Button(self.frame, font=self.game.body13, activebackground="black", activeforeground="white")

        # Player equipped 2
        self.btn_attack2 = tk.Button(self.frame, font=self.game.body13, activebackground="black", activeforeground="white")
    
    def command_items(self):
        self.hide_battleButtons()
        self.game.after(500, self.show_battleButtons)

    def command_draw(self):
        self.drawClicked = True
        self.hide_battleButtons()
        self.game.after(500, self.show_battleButtons)

    def command_attack(self):
        self.hide_battleButtons()
        self.show_attackOptions()

    def command_inspect(self):
        self.inspectClicked = True
        self.hide_battleButtons()
        self.game.after(500, self.show_battleButtons)

    def command_talk(self):
        self.hide_battleButtons()
        self.game.after(500, self.show_battleButtons)

    def command_run(self):
        self.hide_battleButtons()
        self.game.battleModule.endBattle(3)
        self.game.changePage(self.game.page_main)

    # Function that dhoes the battle buttons based on if the draw or inspect buttons have already been pressed
    def show_battleButtons(self):
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
    def hide_battleButtons(self):
        self.btn_items.place_forget()
        self.btn_draw.place_forget()
        self.btn_attack.place_forget()
        self.btn_inspect.place_forget()
        self.btn_talk.place_forget()
        self.btn_run.place_forget()

    # Function that creates the attack UI and starts the attack animation
    def attackSequence(self, chosenItem):

        # Create battle UI
        self.damageModifier = self.background.create_image(480, 470, image=self.game.imageModule.damageModifier, anchor="center")
        self.playerRect = self.background.create_rectangle(100, 420, 118, 520, fill="grey", outline="black", width=7)

        # Start animation
        self.game.after(500, lambda: self.attackAnimation(chosenItem))

    # Function that shows the users options for choosing an attack
    def show_attackOptions(self):

        # Configure buttons
        self.btn_attack1.config(text=self.game.player.equipped[0].details(1),
                                bg=self.game.player.equipped[0].color,
                                command=lambda: self.game.battleModule.playerAttack(self.game.player.equipped[0]))

        self.btn_attack2.config(text=self.game.player.equipped[1].details(1), 
                                bg=self.game.player.equipped[1].color, 
                                command=lambda: self.game.battleModule.playerAttack(self.game.player.equipped[1]))

        # Show buttons
        self.btn_attack1.place(x=20, y=430, width=920, height=40, anchor="nw")
        self.btn_attack2.place(x=20, y=480, width=920, height=40, anchor="nw")

    def hide_attackOptions(self):
        self.btn_attack1.place_forget()
        self.btn_attack2.place_forget()

    # Recursive function that moves the player rect until a spacebar input stops it
    def attackAnimation(self, chosenItem, xOffset=0):
        self.animationActive = True

        # Stop at 735 pixels from starting position
        if xOffset >= 735:
            self.spacebarPressed = True

        # Offset the player rect by 10 pixels
        self.background.move(self.playerRect, 10, 0)
        xOffset += 10

        # If spacebar not clicked, recall function every 15ms
        if not self.spacebarPressed:
            self.game.after(15, lambda: self.attackAnimation(chosenItem, xOffset))

        # If spacebar clicked, set it back to false and detete the battle UI
        else:
            self.spacebarPressed = False
            self.animationActive = False
            x1, y1, x2, y2 = self.background.coords(self.playerRect)
            self.game.battleModule.setModifier(x1+10)
            self.game.battleModule.calculatePlayerDamage(chosenItem)
            self.update()
            self.game.after(500, lambda: self.background.delete(self.damageModifier))
            self.game.after(500, lambda: self.background.delete(self.playerRect))
            

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
        if event.keysym == "space" and self.animationActive:
            self.spacebarPressed = True

    # Function that deals with keyboard releases
    def on_key_release(self, event):
        pass