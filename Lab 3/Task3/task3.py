#The algorithm used in this code is inefficient
def binarySrc(arr,k):

    mid = len(arr)//2
    if len(arr) == 0:
        return 0
    if arr[-1] < k:
        return len(arr)
    if arr[mid] == k:
        return len(arr[:mid])
    if arr[mid] > k:
        return binarySrc(arr[:mid],k)
    if arr[mid] < k:
        return len(arr[:mid+1]) + binarySrc(arr[mid+1:],k)
    
f = open("input3.txt","r")
f1 = open("output3.txt","w")
size = int(f.readline())
l1 = f.readline().split()
l1 = [int(i) for i in l1]
count = 0

for i in range(size):
    temp = sorted(l1[i+1:])
    count += binarySrc(temp,l1[i])
    
f1.write(str(count))
f.close()
f1.close()        




