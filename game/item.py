# Class that defines a singular item
class Item:
    itemIDVariable = 0
    def __init__(self, name: str, rarity: int, pointValue: float, weapon: bool = False, equipable: bool = False, consumable: bool = False):

        self.itemID = self.getItemID()

        self.name = name
        self.rarity = rarity
        self.pointValue = pointValue
        self.weapon = weapon
        self.equipable = equipable
        self.consumable = consumable

        colors = ["grey", "green", "blue", "purple", "Yellow", "cyan", "red"]
        for i in range(len(colors)):
            if self.rarity == i:
                self.color = colors[i]

    # Function that sets the item id based on what items have been created prior
    def getItemID(self) -> str:
        if Item.itemIDVariable // 10 == 0:
            string = "00" + str(Item.itemIDVariable)
        elif Item.itemIDVariable // 100 == 0:
            string = "0" + str(Item.itemIDVariable)
        else:
            if Item.itemIDVariable // 1000 > 0:
                string = "ERR"
            else:
                string = str(Item.itemIDVariable)

        Item.itemIDVariable += 1
        return string

    # Printing the item gives a string that
    def __str__(self):
        return self.name + "; PTV: " + str(self.pointValue)

# Class that defines all the items in the game
class Items:
    def __init__(self, game):
        self.game = game
        self.items = []

        self.spear = Item("Spear", 0, 25, weapon=True); self.items.append(self.spear)
        self.bow = Item("Bow", 0, 35, weapon=True); self.items.append(self.bow)