from typing import List
from typing import Dict

from Classes.DataStorage.DataController import DataController
from Classes.DataStorage.Athlete import Athlete
from Classes.DataStorage.Date import Date
from Classes.Interfaces.InterfaceTemplate import InterfaceTemplate

class CreateAthleteInterface(InterfaceTemplate):
    # Props
    
    RequiredInformation: List[str] = [
        "************",
        "Half As Good",
        "Please enter all of the following information sequentially: ",
        "The athlete's name (all caps, first and last; i.e. CHRISTOPHER STACKPOLE)",
        "The day the athlete was born (just the day; i.e. 28)",
        "The month the athlete was born (just the month; i.e. 8)",
        "The year the athlete was born (just the year; i.e. 2006)",
        "************"
    ]
    
    DisplayOptions: Dict[str, str] = {
        "" : ""
    }
    
    # Methods
    
    # Custom DisplayInterface method, contains some input handling
    def DisplayInterface(self):
        athlete = Athlete(None, None, None)
        for output in self.RequiredInformation:
            print(output)
        
        inp = input()
        athlete.Name = inp
        
        date = Date(None, None, None)
        date.Day = int(input())
        date.Month = int(input())
        date.Year = int(input())
        
        athlete.Birthday = date
        
        # Register the athlete's existence
        DataController.LogAthlete(athlete)
        
        print("Athlete sucessfully created! " + athlete.Name + " was born on " + str(date) + ".")
        
        return