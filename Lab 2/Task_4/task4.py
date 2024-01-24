def insertionSort(arr,idx):
    for i in range(1, len(arr)):
        key = arr[i][idx]
        temp = arr[i]
        j = i-1
        while j >= 0 and key < arr[j][idx] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp  
    return arr


f = open("input4.txt",'r')
f1 = open("output4.txt",'w')

n1,players = f.readline().split(',')
n1, players = int(n1), int(players)
arr = []
for i in range(n1):
    x,y = f.readline().split(',')
    arr.append((int(x),int(y)))


first_arr = insertionSort(arr,0) #Sorted based on 0-th index
first_arr = first_arr[:]
# had to copy the lists because they kept changing for unknown reason
second_arr = insertionSort(arr,1)#Sorted based on 1-th index
second_arr = second_arr[:]

n = n1
l1 = []
l2 = []

for player in range(players):
    i,prev = 1, 0
    if first_arr[prev] not in l1:
        l1.append(first_arr[prev])
    while i < n1:
        if first_arr[i] not in l1 and first_arr[i][0] >= first_arr[prev][1]:
            
            l1.append(first_arr[i])
            prev = i
        else:
            i += 1
    for x in l1:
        if x in first_arr:
            first_arr.remove(x)
            n1 -= 1

for player in range(players):
    i,prev = 1, 0
    if second_arr[prev] not in l2:
        l2.append(second_arr[prev])
    while i < n1:
        if second_arr[i] not in l2 and second_arr[i][0] >= second_arr[prev][1]:
            l2.append(second_arr[i])
            prev = i
        else:
            i += 1
    for x in l2:
        if x in second_arr:
            second_arr.remove(x)
            n -= 1

f1.write(str(max(len(l1),len(l2))))
f.close()
f1.close()