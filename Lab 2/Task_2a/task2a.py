f = open("input2a.txt",'r')
f1 = open("output2a.txt",'w')

n1 = int(f.readline())

l1 = [int(i) for i in f.readline().split()]
n2 = int(f.readline())
l2 = [int(i) for i in f.readline().split()]

l3 = sorted(l1 + l2)

for i in range(len(l3)):
  f1.write(f"{l3[i]} ")

f.close()
f1.close()