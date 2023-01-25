arr=[[1,2,3],
     [4,5,6],
     [7,8,9]] 
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]    
for i in range(len(arr)):
    for j in range(len(arr[0])): 
        result[j][i]=arr[i][j] 
for r in result: 
    print(r)          