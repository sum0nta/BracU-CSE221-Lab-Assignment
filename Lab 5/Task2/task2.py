from collections import deque
def bfs(graph,st=1,arr=[]):
    q = deque()
    for i in graph:
        if graph[i]['indegree'] == 0:
            q.append(i)
    
    while q:
        u = min(q)
        q.remove(u)
        arr.append(u)
        for v in graph[u]["Adj"]:
            graph[v]['indegree'] -= 1
            if graph[v]['indegree'] == 0:
                q.append(v)

    return arr

indegree = []
graph = {}
file = open("input2.txt","r")
f1 = open("output2.txt","w")
vertices, edges = [int(i) for i in file.readline().split()]
graph = {}
for i in range(1,vertices+1):
    graph[i] = {'color':'white',"Adj":[]}

for i in range(edges):
    u, v = [int(i) for i in file.readline().split()]
    
    graph[u]["Adj"].append(v)

for i in range(vertices):
    indegree.append(0)

for i in range(1,vertices+1):
    for j in graph:
        if i in graph[j]["Adj"]:
            indegree[i-1] += 1

for i in range(1,vertices+1):
    graph[i]['indegree'] = indegree[i-1]


x = bfs(graph,1, [])
if len(x) != vertices:
    f1.write("IMPOSSIBLE")
else:
    for i in x:
        f1.write(str(i)+" ")

file.close()
f1.close()