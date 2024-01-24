import heapq
def length(graph,u,v):
    for x in graph[u]['Adj']:
        if x == v:
            return int(x[1])

def dijkstra(graph, st):
    dist = [float("inf")]* len(graph)
    prev = [None] * len(graph)
    dist[st-1] = 0
    q = [(0,st)]
    visited = [False]* len(graph)
    while q:
        cost, vertice = heapq.heappop(q)
        if visited[vertice-1]:
            continue
        visited[vertice-1] = True
        for v in graph[vertice]['Adj']:
            alt = dist[vertice-1] + length(graph,vertice,v)
            
            if alt < dist[v[0]-1]:
                dist[v[0]-1] = alt
                prev[v[0]-1] = vertice
                heapq.heappush(q,[alt,v[0]])
    return dist


f = open("input2.txt","r")
f1 = open("output2.txt","w")
vertices, edges = [int(i) for i in f.readline().split()]
graph = {}
for i in range(1,vertices+1):
    graph[i] = {"Adj":[]}

for i in range(edges):
    u, v, cost = [int(i) for i in f.readline().split()]
    graph[u]["Adj"].append((v,cost))

first,sec = [int(i) for i in (f.readline().split())]
x = dijkstra(graph,first)
y = dijkstra(graph,sec)
i = 0
time = float("inf")
node = None

while i < len(graph):
    if x[i] < time and y[i] < time:
        if x[i] >= y[i]:
            time = x[i]
            node = i+1
        else:
            time = y[i]
            node = i+1
    i += 1

if time == float('inf'):
    f1.write("Impossible")
else:
    f1.write(f"Time {time} \nNode {node}")

f.close()
f1.close()