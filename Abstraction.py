from abc import ABC, abstractmethod 
class vehicle(ABC): 
    @abstractmethod
    def cars(self): 
       pass 
    @abstractmethod
    def bikes(self):
       pass 
class supra_car(vehicle):  
    def cars(self):
        print("supra") 
    def bikes(self):
        pass 
class yamaha_bike(vehicle):
    def cars(self):
        pass
    def bikes(self):
        print("yamaha") 
obj=yamaha_bike()
obj.bikes()         
               
