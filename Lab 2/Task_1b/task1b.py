def targetFinder(arr,n,target):
  f,e = 0, n-1

  for i in range(n):
    if f >= e:
      return "IMPOSSIBLE"
    if arr[f] + arr[e] == target:
      return f"{f+1} {e+1}"
    elif arr[f] + arr[e] < target:
      f += 1
    elif arr[f] + arr[e] > target:
      e -= 1
f = open("input1b.txt",'r')
f1 = open("output1b.txt",'w')
n, target = f.readline().split()
n, target = int(n), int(target)
arr = f.readline().split()
arr = [int(i) for i in arr]
x = targetFinder(arr,n,target)
f1.write(x)
f.close()
f1.close()