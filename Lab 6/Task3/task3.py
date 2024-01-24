def count(arr,x):
    counter = 0
    for i in arr:
        if i == x:
            counter += 1
    return counter

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


f = open("input3.txt","r")
f1 = open("output3.txt","w")
element, edge = [int(i) for i in f.readline().split()]
par = [None]*element
counter = []
for i in range(element):
    par[i] = i + 1

for x in range(edge):
    a,b = [int(i) for i in f.readline().split()]
    x = union(par,a,b)
    counter.append(count(par,x))
    
for i in counter:
    f1.write(str(i)+"\n")

f.close()
f1.close()