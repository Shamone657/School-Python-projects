class Climber:
    
    def __init__ (self,age,equipment,rations,weather,events):
        
       self.age = age
       self.equipment = equipment
       self.rations = rations
       self.weather = weather
       self.events = events


    def info(self):       
        return(f"Climber is {self.age} years old, was {self.equipment}, carried {self.rations}, experienced {self.weather} weather and experienced {self.events}.")
       
