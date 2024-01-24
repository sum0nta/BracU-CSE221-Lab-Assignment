def quickSort(A,p,r,k):
    if p < r:
        q = partition(A,p,r)
        if q == k:
            return A[q]
        elif q > k:
            quickSort(A,p,q-1,k)
        else:
            quickSort(A,q+1,r,k)
    return A[k-1]

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1

f = open("input6.txt","r")
f1 = open("output6.txt","w")
size = int(f.readline())
l1 = f.readline().split()
l1 = [int(i) for i in l1]
qNum = int(f.readline())
for i in range(qNum):
   x = int(f.readline())
   f1.write(str(quickSort(l1,0,size-1,x))+ "\n")

f.close()
f1.close()