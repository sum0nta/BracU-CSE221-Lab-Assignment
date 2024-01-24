from collections import deque

def BFS(graph, start):
    for u in graph:
        graph[u]['color'] = 0
        graph[u]['parent'] = None

    Q = deque()
    graph[start]['color'] = 1
    Q.append(start)
    
    while Q:
        u = Q.popleft()
        for v in graph[u]['Adj']:
            if graph[v]['color'] == 0: 
                graph[v]['color'] = 1
                graph[v]['parent'] = u 
                Q.append(v) 
    

f = open("input5_1.txt","r")
f1 = open("output5_1.txt","w")
l1 = f.readline().split()
n,edges,des = [int(i) for i in l1]
d1 = {}
for i in range(n+1):
    d1[i] = {'color':0, 'Adj':[]}

for x in range(edges):
    l1 = f.readline().split()
    u,v = [int(i) for i in l1]
    if v not in d1[u]['Adj']:
        d1[u]['Adj'].append(v)
    if u not in d1[v]['Adj']:
        d1[v]['Adj'].append(u)


BFS(d1,1)
path = [des]
count = 0
while True:
    x = d1[des]['parent']
    if x == None:
        break
    path.append(x)
    count += 1
    des = x
path = path[::-1]
f1.write("Time: "+ str(count)+ "\n"+ "Shortest Path: ")
for i in path:
    f1.write(f"{i} ")

f.close()
f1.close()



