import numpy as np
f = open("input1a_1.txt","r")
f1 = open("output1a_1.txt","w")

l1 = f.readline().split()
n,edge = [int(i) for i in l1]
arr = np.zeros((n+1,n+1), dtype = int)


for i in range(edge):
    x = f.readline().split()
    first,second,weight = [int(i) for i in x]
    arr[first][second] = weight

for i in range(n+1):
    for j in range(n+1):
        f1.write(str(arr[i][j])+" ")
        
    f1.write("\n")

f.close()
f1.close()