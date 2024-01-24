def bubbleSort(arr):
    for i in range(len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr
'''From the time complexity of sorting algorithms, we know that insertion sort
has time complexity of O(n) in the best case scenerio hence why I modified the
given code into a insertion sort. The reason behind it being O(n) is the fact that
the first loop runs N-times regardless of the inputs so in the best case scenerio
where the input is a sorted array, the inner while loop would not need to be executed
hence the first for loop will run N-times and all the operations within the loop are 
constant time operations therfore, the time complexity will be O(n)'''

f = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_2/input2.txt","r")
f1 = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_2/output2.txt","w")

s = int(f.readline())
arr = f.readline().split()
arr = bubbleSort([int(i) for i in arr])

for i in range(s):
    f1.write(f"{arr[i]} ")

f.close()
f1.close()