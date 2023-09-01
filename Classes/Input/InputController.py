from typing import Dict

from Classes.DataStorage.DataController import SystemData

class InputController:
    # Props
    
    # Methods
    
    def TakeInputAndReturn(self, modifier):
        inp = input()
        inp = modifier(inp)

        if inp == None:
            return self.TakeInputAndReturn(modifier)

        return inp
    
    # Takes input and returns a value, but has the ability to change the screen
    def TakeInputAndReturn_SCREEN_CHANGER(self, modifier, caller):
        inp = input()
        inp = modifier(inp)

        if inp == None:
            return self.TakeInputAndReturn_SCREEN_CHANGE(modifier, caller)
        elif type(inp):
            return

        return inp