from typing import Type

import os
import HalfAsGood

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

mi = HalfAsGood.MainInterface()
mi.DisplayInterface()

toRender = mi.DisplayInterface
inputHandler = mi

class Main:
    # Props

    # Methods
    def change_screen(self, new_screen: Type[HalfAsGood.InterfaceTemplate], return_screen: Type[HalfAsGood.InterfaceTemplate]):
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        # Display newly naviageted screen
        inputHandler = new_screen
        toRender = inputHandler.DisplayInterface
        new_return = toRender(self)
        
        # If new screen returned a screen, navigate to that screen
        if new_return != None:
            self.change_screen(new_return, inputHandler)
            
        # Redisplay previous screen
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        inputHandler = return_screen
        toRender = inputHandler.DisplayInterface
        toRender()

    def __init__(self):
        while True:
            # Handle input and set destination
            inp = input()
            os.system("clear")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            
            inputHandler = inputHandler.HandleInput(inp)
            toRender = inputHandler.DisplayInterface
            
            # If render function returns a value, it is a new screen (subscreen) to navigate to
            new_screen = toRender()
            if new_screen != None:
                self.change_screen(new_screen, inputHandler)