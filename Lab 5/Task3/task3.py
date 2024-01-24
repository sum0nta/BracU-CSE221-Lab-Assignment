#Step 1 [Topological Order]
class Tracker:
    def __init__(self):
        self.time = 0
        self.scc = []

def dfs(graph,t1):
    for u in graph:
        graph[u]['color'] = 'white'
        graph[u]['transpose'] = []
    t1.time = 0
    for u in graph:
        if graph[u]['color'] == 'white':
            dfsVisit(graph,u)

def dfsVisit(graph,u):
    graph[u]['color'] = 'gray'
    t1.time += 1
    for v in graph[u]["Adj"]:
        if graph[v]['color'] == 'white':
            dfsVisit(graph,v)
    graph[u]['color'] = 'black'
    t1.time += 1
    finish[u] = t1.time
#Step 2 [Transpose]
def transpose(graph):
    for i in graph:
        for x in graph[i]['Adj']:
            graph[x]['transpose'].append(i)

#Step 3 [DFS on Transposed Graph]

def dfsT(graph,t2,top):
    for u in graph:
        graph[u]['visited'] = False
    t2.time = 0
    for u in top:
        temp = [u]
        if graph[u]['visited'] == False:
            graph[u]['visited'] = True
            dfsVisited(graph,u,t2,temp)
            t2.scc.append(temp)

def dfsVisited(graph,u,t2,temp):
    t2.time += 1
    
    for v in graph[u]["transpose"]:
        if graph[v]['visited'] == False:
            temp.append(v)
            graph[v]['visited'] = True
            dfsVisited(graph,v,t2,temp)
    t2.time += 1
    finished[u] = t2.time


finish = {}
finished = {}
file = open("input3.txt","r")
f1 = open("output3.txt","w")
vertices, edges = [int(i) for i in file.readline().split()]
graph = {}
for i in range(1,vertices+1):
    graph[i] = {'color':None,"Adj":[]}

for i in range(edges):
    u, v = [int(i) for i in file.readline().split()]
    graph[u]["Adj"].append(v)
t1 = Tracker()
t2 = Tracker()
dfs(graph,t1)
top_ord = sorted(finish, key=finish.get, reverse=True)
transpose(graph)
dfsT(graph,t2,top_ord)

for i in t2.scc:
    for j in sorted(i):
        f1.write(str(j)+ " ")
    f1.write("\n")
file.close()
f1.close()