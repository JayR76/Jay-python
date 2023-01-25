n=int(input("numner"))
if 0< n <20:
  if n%2==0: 
    print("weird")
  else:
      print("normal")
elif n>=20 and n<30:
    print("fast")
elif n>=30:
    if n%2!=0:
      print("normal") 
    else:
         print("wierd")
