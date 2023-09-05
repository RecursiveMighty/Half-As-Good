from typing import Dict

from Classes.DataStorage.DataController import SystemData
from Classes.Interfaces.InterfaceTemplate import InterfaceTemplate

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
    def TakeInputAndReturn_SCREEN_CHANGER(self, modifier, main, return_screen):
        inp = input()
        inp = modifier(inp, main)

        if inp == None:
            return self.TakeInputAndReturn_SCREEN_CHANGER(modifier, main, return_screen)
        elif isinstance(inp, InterfaceTemplate):
            main.change_screen(inp, return_screen)

        return inp