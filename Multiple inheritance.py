class Sun: 
    def Elements(self): 
        print("all are one") 
class Moon: 
     def Elements(self): 
         print("Thanos") 
class Earth(Sun,Moon): 
      pass  
obj=Earth() 
obj.Elements() 
                    