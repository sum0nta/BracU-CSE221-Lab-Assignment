f = open("input1b_1.txt","r")
f1 = open("output1b_1.txt","w")

l1 = f.readline().split()
n,edge = [int(i) for i in l1]

d1 = {}
for i in range(n+1):
    d1[i] = []

for i in range(edge):
    x = f.readline().split()
    first,second,weight = [int(i) for i in x]
    d1[first].append((second,weight))

for i in d1:
    f1.write(str(i)+" : ")
    for j in d1[i]:
        f1.write(str(j)+ " ")
    f1.write("\n")

f.close()
f1.close()