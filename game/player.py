# Class that defines all of the player variables
class Player:

    # Contructor
    def __init__(self, data):

        # Set as variables to access in the future
        self.keys = ["name", "time", "zone", "area"]
        self.data = data

        # using a for loop to create most of the player values effectively using a data list and a keys list
        for key, value in zip(self.keys, self.data):
            setattr(self, key, value)

        # Variables that do not come from a save file
        self.currentArea = self.area
