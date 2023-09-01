from typing import List

class InterfaceTemplate:
    # Props
    
    DisplayBasics: List[str] = ["************", "Half as Good", "************"]
    
    # Methods
    
    def DisplayInterface(self):
        print(self.DisplayBasics[0])
        print(self.DisplayBasics[1])
        for key in self.DisplayOptions:
            print(self.DisplayOptions[key], key)
        print(self.DisplayBasics[2])
        
        return
    
    def HandleInput(self, inp: str):
        return self.OptionDestinations[inp]()