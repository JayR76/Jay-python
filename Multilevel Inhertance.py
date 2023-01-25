class college: 
     name="aditya" 
     locate="surampalem" 
     phone=6767 
class principal(college): 
     name="Babu" 
     phone=3456  
class Hod(principal): 
     name="prasad" 
     locate="pedapuram" 
class Staff(Hod): 
     name="gani" 
print(Hod.name) 
print(principal.phone)     