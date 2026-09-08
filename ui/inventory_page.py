from resources.page import Page

class InventoryPage(Page):
    def __init__(self, game):
        super().__init__(game, game.frame_inventory, game.imageModule.z1Backgrounds[0])

    # Abstract update function to provide every child with update functionality
    def update(self):
        pass

    # Abstract function that deals with the users keyboard presses depending on each page
    def on_key_press(self, event):
        pass

    # Abstract function that deals with the users keyboard releases depending on each page
    def on_key_release(self, event):
        pass