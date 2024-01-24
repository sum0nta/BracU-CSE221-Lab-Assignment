def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid]) 
    a2 = mergeSort(arr[mid:]) 
    if a1 > a2:
      return a1
  return a2

# Time complexity of this code is O(Nlog(n))

f = open("input2.txt","r")
f1 = open("output2.txt","w")

size = int(f.readline())
l1 = f.readline().split()
l1 = [int(i) for i in l1]

l1 = mergeSort(l1)

for i in l1:
  f1.write(f"{i}")

f.close()
f1.close()