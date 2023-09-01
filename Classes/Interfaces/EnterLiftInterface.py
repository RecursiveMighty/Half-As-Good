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
    def DisplayInterface(self):
        ic = InputController()
        
        lift = Record(None, None, None, None)
        for output in self.RequiredInformation:
            print(output)
        
        # Get lift name, then find enum
        lift_name = input()
        for enum in LiftEnums:
            if enum.name == lift_name:
                lift.LiftType = enum.value
        """      
        lift.LiftType = ic.TakeInputAndReturn(
            def func(*params):
                for enum in LiftEnums:
                    if enum.name == params.inp[0]:
                        params.target = enum.value
            )
            
        lift.LiftType = ic.TakeInputAndReturn(() => {
            ...
        })
        """
                
                
        # Handling if the lift isn't tracked
        if lift.LiftType == None:
            print("That lift is not tracked by the system")
            return
        
        # Get athlete name, then find ID or prompt creating new athlete
        athlete_name = input()
        athletes = SystemData["Athletes"]
        for athleteID in athletes:
            if athlete_name == athletes[athleteID].Name:
                lift.Athlete = athletes[athleteID].Name
                
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
        
        lift.Weight = float(input())
        
        print("Lift successfully created! " + lift.Athlete + " lifted " + str(lift.Weight) + " lbs, in a " + LiftEnums.GetNameFromValue(LiftEnums, lift.LiftType))