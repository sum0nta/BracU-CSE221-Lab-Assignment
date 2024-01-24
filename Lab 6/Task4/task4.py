def insertionSort(arr,idx):
    for i in range(1, len(arr)):
        key = arr[i][idx]
        temp = arr[i]
        j = i-1
        while j >= 0 and key < arr[j][idx] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp  
    return arr
def find(par,r):
    if par[r-1] == r:
        return r
    return find(par,par[r-1])

def union(par,a,b):
    u = find(par,a)
    v = find(par,b)
    if u != v:
        for i in range(len(par)):
            if par[i] == u:
                par[i] = v
    return v

f = open("input4.txt","r")
f1 = open("output4.txt","w")
y = []
vertices, edges = [int(j) for j in f.readline().split()]
for i in range(edges):
    x = [int(j) for j in f.readline().split()]
    y.append(x)

insertionSort(y,2)
par = [None]*vertices
cost = 0

for i in range(vertices):
    par[i] = i + 1

for i in y:
    if par[i[0]-1] != par[i[1]-1]:
        cost += i[2]
        union(par,par[i[0]-1], par[i[1]-1])

f1.write(str(cost))

f.close()
f1.close()