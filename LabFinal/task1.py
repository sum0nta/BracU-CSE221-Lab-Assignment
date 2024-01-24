#Question - 1
f = open("input1.txt","r")
f1 = open("output1.txt","w")
graph = {}
verices = int(f.readline())
edges = int(f.readline())

#Question - 2
for i in range(edges):
    m,n = [i for i in f.readline().split("^")]
    if m not in graph:
        graph[m] = [n.strip()]
    else:
        graph[m].append(n.strip())
f1.write("Adjacency List:" +"\n")
for i in graph:
    f1.write(i+": ")
    for x in graph[i]:
        f1.write(x+" ")
    f1.write("\n")

#Question - 3
class Tracker:
    def __init__(self):
        self.path = []
def search(st,graph,end,t1):
    if st == end:
        t1.path.append(st)
        return t1.path
    for i in graph[st]:
        t1.path.append(st)
        return search(i,graph,end,t1)

t2 = Tracker()
l1 = search("A",graph,"I",t2)
f1.write("Output of Q3:"+"\n")
for i in l1[:-1]:
    f1.write(str(i)+", ")
f1.write(str(l1[-1])+"\n")

#Question - 4
def search(st,graph,end,t1,police):
    if st == end:
        t1.path.append(st)
        return t1.path
    for i in graph[st]:
        if st == police or i == police:
            continue
        t1.path.append(st)
        return search(i,graph,end,t1,police)

t3 = Tracker()
l1 = search("A",graph,"I",t3,"D")
f1.write("Output of Q4:"+"\n")
for i in l1[:-1]:
    f1.write(str(i)+", ")
f1.write(str(l1[-1]))

f.close()
f1.close()