# Class that defines all of the player variables
class Player:

    # Contructor
    def __init__(self):

        # Set as variables to access in the future
        self.keys = ["name", "time", "zone", "area", "level", "exp", "equipped", "inventory"]

    # Function that actually sets all of the player variables
    def setStats(self, data):
        self.data = data
        
        # using a for loop to create most of the player values effectively using a data list and a keys list
        for key, value in zip(self.keys, self.data):
            setattr(self, key, value)

        # Variables that do not come from a save file
        self.currentArea = self.area

    # String that is returned when str(Player) is called
    def __str__(self):
        string = ""
        for key, value in zip(self.keys, self.data):
            length = len(key) + 1
            string += key.capitalize() + ":"
            for i in range(12 - length):
                string += " "

            # Equipped data
            if key == self.keys[len(self.keys)-2]:
                string += str(value[0]) + ", " + str(value[1]) + "\n"

            # Inventory data
            elif key == self.keys[len(self.keys)-1]:
                for i in range(len(value)):
                    if i == len(value) - 1:
                        string += str(value[i]) + "\n"
                    else:
                        string += str(value[i]) + ", "

            # Normal data
            else:
                string += str(value) + "\n"
        
        return string
            