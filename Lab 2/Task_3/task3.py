def insertionSort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i][1]
        temp = arr[i]
        j = i-1
        while j >= 0 and key < arr[j][1] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


f = open("input3.txt",'r')
f1 = open("output3.txt",'w')

n1 = int(f.readline())
arr = []
for i in range(n1):
    x,y = f.readline().split()
    arr.append((int(x),int(y)))

arr = insertionSort(arr)

i,prev = 1, 0
x,y = arr[prev]
str1 = f"{x} {y}" + "\n"
num = 1
while i < n1:
    if arr[i][0] >= arr[prev][1]:
        x,y = arr[i]
        str1 += f"{x} {y}" + "\n"
        num += 1
        prev = i
    i += 1
str1 = str(num) + "\n" + str1
f1.write(str1)
f.close()
f1.close()