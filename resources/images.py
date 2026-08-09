import tkinter as tk
from pathlib import Path

# class that creates all of the images
class Images:
    def __init__(self):

        # Constant folder paths
        DATA_FOLDER = Path("data")
        BACKGROUNDS_FOLDER = DATA_FOLDER / "resouces" / "backgrounds"
        BG_ZONE1_FOLDER = BACKGROUNDS_FOLDER / "zone1"
        BG_ZONE2_FOLDER = BACKGROUNDS_FOLDER / "zone2"
        SPRITES_FOLDER = DATA_FOLDER / "resouces" / "sprites"

        # Zone 1 backgrounds

        self.bg_z1a0 = tk.PhotoImage(BG_ZONE1_FOLDER / "image0.png")

        self.z1Backgrounds = []

        for i in range(1, 11):
            background = tk.PhotoImage(BG_ZONE1_FOLDER / f"image{i}.png")
            self.z1Backgrounds.append(background)

        self.bg_z1b1 = tk.PhotoImage(BG_ZONE1_FOLDER / "image11.png")