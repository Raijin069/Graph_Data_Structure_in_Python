def sssP(graph,node,d,distance,par):
    distance[node]  = d

edges = []
nodes = []    

graph = {}
distance = {}
for key in nodes:
    graph[key] = []
    distance[key] = None

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)

start = "A"
distance[start] = 0
sssP(graph,start,0,distance,-1)
print(graph)    
