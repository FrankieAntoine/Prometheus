from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.game import Game

from pathlib import Path

# Class that manages all of the saving in the game
class SaveManger:

    # Constructor
    def __init__(self, game: Game):

        self.game = game

        SAVES_FOLDER = Path("data/saves")
        self.savePaths = [
            SAVES_FOLDER / "save1.txt", 
            SAVES_FOLDER / "save2.txt", 
            SAVES_FOLDER / "save3.txt"
        ]

        self.save1Data = [] # List to store the data from file 1
        self.save2Data = [] # List to store the data from file 2
        self.save3Data = [] # List to store the data from file 3
        self.savesData = [self.save1Data, self.save2Data, self.save3Data]

        # Function that grabs that sets the data lists
        self.loadSaves()
        
    # Function that loads all of the save data into the save data lists
    def loadSaves(self):
        for dataList, saveFile in zip(self.savesData, self.savePaths):
            with open(saveFile, "r") as file:
                for line in file:
                    dataList.append(line.rstrip("\n"))

    # Function that takes the raw data from a specific save file and returns the configured data list
    def configData(self, dataList) -> list:
        dataList[0] = str(dataList[0])
        for i in range(1, 6):
            dataList[i] = int(dataList[i])
        dataList[len(dataList) - 2] = eval(dataList[len(dataList) - 2])
        dataList[len(dataList) - 1] = eval(dataList[len(dataList) - 1])
        return dataList

    # Function that given a save number returns the player object
    def loadPlayer(self, saveNumber):
        self.game.player.setStats(self.configData(self.savesData[saveNumber-1]))
        self.loadFromID(self.game.player.inventory)
        self.loadFromID(self.game.player.equipped)
        self.game.page_main.update()
        print(self.game.player)

    # Function that loads the inventory and equipped items of the player
    def loadFromID(self, listOfIDs):
        for i in range(len(listOfIDs)):
            for j in range(len(self.game.itemModule.items)):
                if listOfIDs[i] == self.game.itemModule.items[j].itemID:
                    listOfIDs[i] = self.game.itemModule.items[j]
