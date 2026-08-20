import tkinter as tk
from pathlib import Path

# class that creates all of the images
class Images:
    def __init__(self):

        # Constant folder paths
        DATA_FOLDER = Path("data")
        BACKGROUNDS_FOLDER = DATA_FOLDER / "resources" / "backgrounds"
        BG_ZONE1_FOLDER = BACKGROUNDS_FOLDER / "zone1"
        BG_ZONE2_FOLDER = BACKGROUNDS_FOLDER / "zone2"
        SPRITES_FOLDER = DATA_FOLDER / "resources" / "sprites"
        ELEMENTS_FOLDER = DATA_FOLDER / "resources" / "elements"

        # Zone 1 spirites
        self.z1Sprites = []

        for i in range(1, 4):
            sprite = tk.PhotoImage(file=SPRITES_FOLDER / f"enemySprite{i}.jpg")
            self.z1Sprites.append(sprite)

        # Zone 1 backgrounds
        self.bg_z1a0 = tk.PhotoImage(file=BG_ZONE1_FOLDER / "image0.png")

        self.z1Backgrounds = []

        for i in range(1, 11):
            background = tk.PhotoImage(file=BG_ZONE1_FOLDER / f"image{i}.png")
            self.z1Backgrounds.append(background)

        self.bg_z1b1 = tk.PhotoImage(file=BG_ZONE1_FOLDER / "image11.png")

        # Game elements
        self.damageModifier = tk.PhotoImage(file=ELEMENTS_FOLDER / "damageModifier.png")