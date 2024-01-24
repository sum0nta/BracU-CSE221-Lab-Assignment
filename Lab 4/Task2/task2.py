from collections import deque

def BFS(graph, start):
    for u in graph:
        graph[u]['color'] = 0

    Q = deque()
    graph[start]['color'] = 1
    Q.append(start)
    path = []

    while Q:
        u = Q.popleft()  
        path.append(u)
        for v in graph[u]['Adj']:  
            if graph[v]['color'] == 0: 
                graph[v]['color'] = 1 
                Q.append(v) 
    return path

f = open("input2_1.txt","r")
f1 = open("output2_1.txt","w")
l1 = f.readline().split()
n,m = [int(i) for i in l1]
d1 = {}
for i in range(n+1):
    d1[i] = {'color':0, 'Adj':[]}

for x in range(m):
    l1 = f.readline().split()
    u,v = [int(i) for i in l1]
    if v not in d1[u]['Adj']:
        d1[u]['Adj'].append(v)
    if u not in d1[v]['Adj']:
        d1[v]['Adj'].append(u)


path = BFS(d1, 1)
for i in path:
    f1.write(str(i) + " ")

f.close()
f1.close()



