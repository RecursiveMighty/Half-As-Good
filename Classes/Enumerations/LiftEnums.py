from enum import Enum

class LiftEnums(Enum):
    # Props
    
    BACKSQUAT = 0
    BENCHPRESS = 1
    DEADLIFT = 2
    FRONTSQUAT = 3
    
    # Methods
    def GetNameFromValue(en, value: int):
        for enum in en:
            if enum.value == value:
                return enum.name
        return None