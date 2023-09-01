from typing import Dict
from typing import Type

from Classes.DataStorage.Athlete import Athlete
from Classes.DataStorage.Record import Record
from Classes.DataStorage.Date import Date
from Classes.Enumerations.LiftEnums import LiftEnums

# For the purposes of effectively tracking all information, all writing to the SystemData should be
# done via the DataController class, not directly (so that Athletes, Records, etc. can be
# initilized with their IDs included by the system), though reading from the SystemData can be done
# anywhere by any file
SystemData: Dict[str, Dict[int, Athlete] or Dict[int, Record]] = {
    "Athletes" : {
        # Athletes initiliazed with form:  (Athlete Name, Date of Birth, ID)
        1 : Athlete("CHRISTOPHER STACKPOLE", Date(28, 8, 2006), 1),
        2 : Athlete("BRIAN SHAW", Date(26, 2, 1982), 2)
    }
}

# Some data must be added outside of the declaration of the SystemData, as it makes reference to data
# written inside of the SystemData (i.e. Records making reference to Athletes defined within the data)

SystemData["Records"] = {
    # Records initiliazed with form: (LiftEnum, Athlete, Weight, ID)
    1 : Record(LiftEnums.BACKSQUAT, SystemData["Athletes"][1], 350, 1),
    2 : Record(LiftEnums.BACKSQUAT, SystemData["Athletes"][2], 901, 2),
    3 : Record(LiftEnums.BENCHPRESS, SystemData["Athletes"][1], 260, 3),
    4 : Record(LiftEnums.BENCHPRESS, SystemData["Athletes"][2], 530, 4)
}

class _DataController:
    # Props
    
    # Methods
    
    @staticmethod 
    def InitializeDataFromFile(file_name: str):
        return
    
    @staticmethod
    def GetAthleteFromID(ID: int):
        return
    
    # Methods for adding data
    
    @staticmethod
    def LogAthlete(athlete: Athlete):
        athletes = SystemData["Athletes"]
        length = len(athletes)
        athlete.ID = length + 1
        athletes[athlete.ID] = athlete
        return
    
    @staticmethod
    def LogLift(record: Record):
        return
    
DataController = _DataController()