import heapq
def length(graph,u,v):
    for x in graph[u]['Adj']:
        if x == v:
            return int(x[1])

def dijkstra(graph, start):
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


f = open("input1.txt","r")
f1 = open("output1.txt","w")
vertices, edges = [int(i) for i in f.readline().split()]
graph = {}
for i in range(1,vertices+1):
    graph[i] = {"Adj":[]}

for i in range(edges):
    u, v, cost = [int(i) for i in f.readline().split()]
    graph[u]["Adj"].append((v,cost))

st = int(f.readline())
for i in dijkstra(graph,st):
    if i == float('inf'):
        f1.write('-1' + " ")
    else:
        f1.write(str(i)+ " ")
f.close()
f1.close()