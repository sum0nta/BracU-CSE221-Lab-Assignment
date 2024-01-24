#The algorithm takes O(n^2*log(n)) time
f = open("input4.txt","r")
f1 = open("output4.txt","w")
size = int(f.readline())
l1 = f.readline().split()
l1 = [int(i) for i in l1]

squared = [i**2 for i in l1]
maximum = -99999
for i in range(size-1):
    temp = squared[:i+1] + (sorted(squared[i+1:])[::-1])
    if (l1[i] + temp[i+1]) > maximum:
        maximum = l1[i] + temp[i+1]
    
f1.write(str(maximum))
f.close()
f1.close()
