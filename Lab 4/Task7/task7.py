def DFS(graph, st, visited, path):
    visited[st] = True
    path.append(st)

    for v in graph[st]:
        if visited[v] == False:
            DFS(graph, v, visited, path)

def nodeFinder(graph, n):
    visited = [False] * (n+1)
    path = []
    DFS(graph, 1, visited, path)
    
    st = path[-1]
    visited = [False] * (n+1)
    path = []
    DFS(graph, st, visited, path)
    
    return st, path[-1]

f = open("input7.txt","r")
f1 = open("output7.txt","w")
n = int(f.readline())
d1 = {}
for i in range(n+1):
    d1[i] = []

for x in range(n-1):
    u, v = [int(i) for i in f.readline().split()]
    d1[u].append(v)
    d1[v].append(u)

st,end = nodeFinder(d1,n)
f1.write(str(st) +" " + str(end))

f.close()
f1.close()