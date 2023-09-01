class Date:
    # Props
    
    Day: int
    Month: int
    Year: int
    
    # Methods
    
    def __init__(self, day: int, month: int, year: int):
        self.Day = day
        self.Month = month
        self.Year = year
        
    def __str__(self):
        day = str(self.Day)
        month = str(self.Month)
        year = str(self.Year)
        
        if self.Day < 10:
            day = "0" + str(self.Day)
        
        if self.Month < 10:
            month = "0" + str(self.Month)
            
        return day + "." + month + "." + year