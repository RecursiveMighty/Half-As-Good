from typing import List

from Classes.DataStorage.Date import Date

class Athlete:
    # Props
    
    Name: str
    Birthday: Date
    ID: int
    
    # Methods
    
    def __init__(self, name: str, birthday: Date, ID: int):
        self.Name = name
        self.Birthday = birthday
        self.ID = ID
    
    def RecordLift():
        return