from typing import Dict

from Classes.Interfaces.InterfaceTemplate import InterfaceTemplate
from Classes.Interfaces.RecordsListInterface import RecordsListInterface
from Classes.Interfaces.PersonalRecordsInterface import PersonalRecordsInterface
from Classes.Interfaces.EnterLiftInterface import EnterLiftInterface
from Classes.Interfaces.CreateAthleteInterface import CreateAthleteInterface

class MainInterface(InterfaceTemplate):
    # Props

    DisplayOptions: Dict[str, str] = {
        "1" : "View Records List:",
        "2" : "View Personal Records:",
        "3" : "Enter New Lift:",
        "4" : "Create New Athlete:"
    }
    
    OptionDestinations = {
        "1" : RecordsListInterface,
        "2" : PersonalRecordsInterface,
        "3" : EnterLiftInterface,
        "4" : CreateAthleteInterface
    }
    
    # Methods