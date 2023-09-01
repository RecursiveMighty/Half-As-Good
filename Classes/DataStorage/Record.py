from Classes.Enumerations.LiftEnums import LiftEnums
from Classes.DataStorage.Athlete import Athlete

class Record():
    # Props
    
    LiftType: LiftEnums
    Athlete: Athlete
    Weight: float
    ID: int
    
    # Methods
    
    def __init__(self, lift_enum, athlete, weight, ID):
        self.LiftType = lift_enum
        self.Athlete = athlete
        self.Weight = weight
        self.ID = ID
        
    @staticmethod
    def KGsToLBs():
        return