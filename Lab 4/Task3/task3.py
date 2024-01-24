def colourInitializing(graph):
    for u in graph:
        graph[u]['color'] = 0
        

def DFS(graph,st,path):
    graph[st]['color'] = 1
    path.append(st)

    for v in graph[st]['Adj']:  
        if graph[v]['color'] == 0: 
            DFS(graph,v,path)
            
f = open("input3_1.txt","r")
f1 = open("output3_1.txt","w")
l1 = f.readline().split()
n,m = [int(i) for i in l1]
d1 = {}
for i in range(n+1):
    d1[i] = {'color':0, 'Adj':[]}

for i in range(m):
    l1 = f.readline().split()
    u,v = [int(i) for i in l1]
    d1[u]['Adj'].append(v)
    d1[v]['Adj'].append(u)

path = []
colourInitializing(d1)
DFS(d1, 1, path)
for i in path:
    f1.write(str(i) + " ")

f.close()
f1.close()