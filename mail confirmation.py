a=input("enter the mail: ")   
if "@gmail.com" in a: 
  if a[0].isalpha(): 
    print("valid") 
  else: 
      print("invalid")  
else: 
    print("doesnt contain")        
      