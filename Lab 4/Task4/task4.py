def colourInitializing(graph):
    for u in graph:
        graph[u]['color'] = 0
        graph[u]['tracker'] = False

def cycleDFS(graph,st):
    graph[st]['color'] = 1
    graph[st]['tracker'] = True

    for v in graph[st]['Adj']: 
        if graph[v]['tracker']:
            return True
        if graph[v]['color'] == 0: 
            if cycleDFS(graph,v):
                return True
    graph[st]['tracker'] = False
    return False
        
            
f = open("input4_4.txt","r")
f1 = open("output4_1.txt","w")
l1 = f.readline().split()
n,m = [int(i) for i in l1]
d1 = {}
for i in range(n+1):
    d1[i] = {'color':0, 'Adj':[]}

for i in range(m):
    l1 = f.readline().split()
    u,v = [int(i) for i in l1]
    d1[u]['Adj'].append(v)


colourInitializing(d1)

if cycleDFS(d1,1):
    f1.write("YES")
else:
    f1.write('NO')


f.close()
f1.close()