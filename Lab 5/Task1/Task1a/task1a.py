def dfsCycle(u, graph):
    graph[u]['visited'] = True
    graph[u]['checker'] = True

    for v in graph[u]["Adj"]:
        
        if not graph[v]['visited']:
            if dfsCycle(v, graph):
                return True
        elif graph[v]['checker']:
            return True

    graph[u]['checker'] = False
    return False

def hasCycle(graph):

    for u in graph:
        graph[u]['visited'] = False
        graph[u]['checker'] = False
    

    for u in graph:
        if not graph[u]['visited']:
            if dfsCycle(u,graph):
                return True

    return False

class Tracker:
    def __init__(self):
        self.time = 0

def dfs(graph):
    for u in graph:
        graph[u]['color'] = 'white'
    Tracker.time = 0

    for u in graph:
        if graph[u]['color'] == 'white':
            dfsVisit(graph,u)

def dfsVisit(graph,u):
    
    graph[u]['color'] = 'gray'
    Tracker.time += 1
    for v in graph[u]["Adj"]:
        if graph[v]['color'] == 'white':
            dfsVisit(graph,v)
    graph[u]['color'] = 'black'
    Tracker.time += 1
    finish[u] = Tracker.time

finish = {}

file = open("input1a.txt","r")
f1 = open("output1a.txt","w")
vertices, edges = [int(i) for i in file.readline().split()]
graph = {}
for i in range(1,vertices+1):
    graph[i] = {'color':None,"Adj":[]}

for i in range(edges):
    u, v = [int(i) for i in file.readline().split()]
    graph[u]["Adj"].append(v)
g1 = graph
if hasCycle(graph):
    f1.write("IMPOSSIBLE")
else:
    dfs(graph)
    top = sorted(finish, key=finish.get, reverse=True)
    for i in top:
        f1.write(str(i)+ " ")

file.close()
f1.close()