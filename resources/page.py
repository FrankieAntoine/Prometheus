import tkinter as tk
from abc import ABC, abstractmethod

# Basic page class that defines each page in the game
class Page(ABC):

    # contructor
    def __init__(self, game, frame, backgroundImage):
        self.game = game
        self.frame = frame
        self.backgroundImage = backgroundImage

        self.background = tk.Canvas(self.frame, highlightthickness=0)
        self.background.pack(fill="both", expand=True)
        self.backgroundImageID = self.background.create_image(0, 0, image=self.backgroundImage, anchor="nw")

    # Function that changes the background image given a new one
    def changeBackgroundImage(self, newImage):
        self.background.itemconfigure(self.backgroundImageID, image=newImage)

    # Making it so the page object can lift instead of calling the frame to lift
    def lift(self):
        self.frame.lift()

    # abstract update function to provide every child with update functionality
    @abstractmethod
    def update(self):
        pass