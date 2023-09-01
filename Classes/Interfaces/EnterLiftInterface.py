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
    def DisplayInterface(self, caller):
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
        
        print(isinstance(CreateAthleteInterface(), CreateAthleteInterface))
        # Get athlete name, then find ID or prompt creating new athlete
        def modifier(inp):
            athletes = SystemData["Athletes"]
            for athleteID in athletes:
                if inp == athletes[athleteID].Name:
                    return athletes[athleteID].Name
            # Athlete was not found
            print("Athlete does not exist. Would you like to create one? (Y or N)")
            temp_inp = input()
            if temp_inp == "Y":
                return [CreateAthleteInterface(), CreateAthleteInterface]
        lift.Athlete = ic.TakeInputAndReturn_SCREEN_CHANGER(modifier, caller)

        """
        # Handle athlete not existing
        if lift.Athlete == None:
            print("Athlete does not exist, would you like to create one? (Y or N)")
            inp = input()
            if inp == "Y":
                return CreateAthleteInterface()
            elif inp == "N":
                needs_valid = True
                while needs_valid == True:
                    print("Please enter a valid athlete name, or enter 1 to create a new athlete.")
                    athlete_name = input()
                    if athlete_name == "1":
                        return CreateAthleteInterface()
                    for athleteID in athletes:
                        if athlete_name == athletes[athleteID].Name:
                            lift.Athlete = athletes[athleteID].Name
                            needs_valid = False
        """
        
        lift.Weight = float(input())
        
        print("Lift successfully created! " + lift.Athlete + " lifted " + str(lift.Weight) + " lbs, in a " + LiftEnums.GetNameFromValue(LiftEnums, lift.LiftType))