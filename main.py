from typing import Type

import os
import HalfAsGood

os.system("clear")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

mi = HalfAsGood.MainInterface()
mi.DisplayInterface()

toRender = mi.DisplayInterface
initInputHandler = mi

class Main:
    # Props

    inputHandler = initInputHandler

    # Methods
    def change_screen(self, new_screen: Type[HalfAsGood.InterfaceTemplate], return_screen: Type[HalfAsGood.InterfaceTemplate]):
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        # Display newly naviageted screen
        self.inputHandler = new_screen
        toRender = self.inputHandler.DisplayInterface
        new_return = toRender(self)
        
        # If new screen returned a screen, navigate to that screen
        if new_return != None:
            self.change_screen(new_return, self.inputHandler)
            
        # Redisplay previous screen
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.inputHandler = return_screen
        toRender = self.inputHandler.DisplayInterface
        toRender(self)

    def __init__(self):
        while True:
            # Handle input and set destination
            inp = input()
            os.system("clear")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            
            self.inputHandler = self.inputHandler.HandleInput(inp)
            toRender = self.inputHandler.DisplayInterface
            
            # If render function returns a value, it is a new screen (subscreen) to navigate to
            new_screen = toRender(self)
            if new_screen != None:
                self.change_screen(new_screen, self.inputHandler)

main = Main()