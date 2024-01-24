def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    return A
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    
    return i+1

f = open("input5.txt","r")
f1 = open("output5.txt","w")
size = int(f.readline())
l1 = f.readline().split()
l1 = [int(i) for i in l1]
l1 = quickSort(l1,0,size-1)
for i in range(len(l1)):
    f1.write(str(l1[i])+ " ")

f.close()
f1.close()