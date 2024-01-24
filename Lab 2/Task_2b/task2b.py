f = open("input2b.txt",'r')
f1 = open("output2b.txt",'w')

n1 = int(f.readline())
l1 = [int(i) for i in f.readline().split()]
n2 = int(f.readline())
l2 = [int(i) for i in f.readline().split()]

l3 = []
i,j = 0,0

while i < n1 and j < n2:
  if l1[i] >= l2[j]:
    l3.append(l2[j])
    j += 1
  else:
    l3.append(l1[i])
    i += 1

l3 += l1[i:]
l3 += l2[j:]
l3 = [str(i) for i in l3]
f1.write(' '.join(l3))
f.close()
f1.close()