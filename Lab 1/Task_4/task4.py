def partition(arr, low, high):
  p = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] <= p:
      i = i + 1

      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quickSort(arr,low,high):
  if low < high:

    p = partition(arr, low, high)

    quickSort(arr, low, p - 1)
    quickSort(arr, p + 1, high)
    return arr
  
def sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j].split()[0] == arr[j+1].split()[0]:
                x = arr[j].split()[-1] 
                y = arr[j+1].split()[-1] 
                if int(x[:2] + x[3:]) < int(y[:2] + y[3:]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


f = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_4/input4.txt","r")
f1 = open("/Users/sumonta/Desktop/LabSection14_22341019_CSE221LabAssignment1_Fall2023/Task_4/output4.txt","w")

s = int(f.readline())
lines = f.readlines()

lines = [i[:len(i)-1] for i in lines[:-1]] + [lines[len(lines)-1]]

lines = sort(quickSort(lines,0,len(lines)-1))

for i in range(s):
    f1.write(lines[i]+"\n")

f1.close()
f.close()