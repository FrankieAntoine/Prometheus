# Class that defines all of the player variables
class Player:

    # Contructor
    def __init__(self):

        # Set as variables to access in the future
        self.keys = ["name", "time", "zone", "area"]

    # Function that actually sets all of the player variables
    def setStats(self, data):
        self.data = data
        
        # using a for loop to create most of the player values effectively using a data list and a keys list
        for key, value in zip(self.keys, self.data):
            setattr(self, key, value)

        # Variables that do not come from a save file
        self.currentArea = self.area

    def __str__(self):
        return str(dict(zip(self.keys, self.data)))