from typing import Type

import os
import HalfAsGood

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

mi = HalfAsGood.MainInterface()
mi.DisplayInterface()

toRender = mi.DisplayInterface
inputHandler = mi

# Handle navigating through n subscreens 
def change_screen(new_screen: Type[HalfAsGood.InterfaceTemplate], return_screen: Type[HalfAsGood.InterfaceTemplate]):
    os.system("clear")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    # Display newly naviageted screen
    inputHandler = new_screen
    toRender = inputHandler.DisplayInterface
    new_return = toRender()
    
    # If new screen returned a screen, navigate to that screen
    if new_return != None:
        change_screen(new_return, inputHandler)
        
    # Redisplay previous screen
    os.system("clear")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    inputHandler = return_screen
    toRender = inputHandler.DisplayInterface
    toRender()

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
       change_screen(new_screen, inputHandler)