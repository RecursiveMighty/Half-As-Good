from typing import List

from Classes.DataStorage.DataController import SystemData
from Classes.DataStorage.Record import Record
from Classes.Enumerations.LiftEnums import LiftEnums
from Classes.Input.InputController import InputController
from Classes.Interfaces.InterfaceTemplate import InterfaceTemplate
from Classes.Interfaces.CreateAthleteInterface import CreateAthleteInterface

class EnterLiftInterface(InterfaceTemplate):
    # Props
    
    RequiredInformation: List[str] = [
        "************",
        "Half As Good",
        "Please enter all of the following information sequentially: ",
        "The name of the lift (all caps, full name; i.e. BACKSQUAT)",
        "The name of the athlete (all caps, full name; i.e. JOHN DOE)",
        "The weight of the lift (in lbs, no units label; i.e. 225)",
        "************"
    ]
    
    OptionDestinations = {
           
    }
    
    # Method
    
    # Specialized DisplayInterface method, contains some input handling
    def DisplayInterface(self, main):
        ic = InputController()
        
        lift = Record(None, None, None, None)
        for output in self.RequiredInformation:
            print(output)
        
        # Get lift name, then find enum
        def modifier(inp):
            for enum in LiftEnums:
                if enum.name == inp:
                    return enum.value
            print("That lift is not recognized by the system.\nPlease reenter the lift name.")
            return None
        lift.LiftType = ic.TakeInputAndReturn(modifier)
        
        # Get athlete name, then find ID or prompt creating new athlete
        def modifier(inp, main):
            athletes = SystemData["Athletes"]
            for athleteID in athletes:
                if inp == athletes[athleteID].Name:
                    return athleteID
            # Athlete was not found
            print("Athlete does not exist. Would you like to create one? (Y or N)")
            temp_inp = input()
            if temp_inp == "Y":
                return CreateAthleteInterface()
            elif temp_inp == "N":
                print("Please enter a valid athlete name.")
                return None
        lift.Athlete = ic.TakeInputAndReturn_SCREEN_CHANGER(modifier, main, self)

        lift.Weight = float(input())
        
        print("Lift successfully created! " + SystemData["Athletes"][lift.Athlete].Name + " lifted " + str(lift.Weight) + " lbs, in a " + LiftEnums.GetNameFromValue(LiftEnums, lift.LiftType))