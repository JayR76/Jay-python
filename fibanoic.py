n=int(input("number:")) 
n1,n2=0,1 
count=0 
if n<=0: 
   print("positive integer")
elif n==0: 
    print("fibanocci series",n,":") 
    print(n1) 
else: 
    print("fibannoic:") 
    while count < n: 
        print(n1) 
        nth=n1+n2 
        n1=n2 
        n2=nth 
        count +=1 
