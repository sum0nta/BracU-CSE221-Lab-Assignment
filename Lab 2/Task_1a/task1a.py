def targetFinder(arr,n,target):
  for i in range(n):
    for j in range(i+1,n):
      if arr[i] + arr[j] == target:
        return f"{i+1} {j+1}"
  return "IMPOSSIBLE"
f = open("input1a.txt",'r')
f1 = open("output1a.txt",'w')
n, target = f.readline().split()
n, target = int(n), int(target)
arr = f.readline().split()
arr = [int(i) for i in arr]
x = targetFinder(arr,n,target)
f1.write(x)
f.close()
f1.close()