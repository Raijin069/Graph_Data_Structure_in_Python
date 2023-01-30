ipt = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]

n = 6

"""

##### with the help of adajcent list #####

graph = {}
for i in range(n):
    graph[i] = []

for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)

for item in graph.items():
    print(item)

"""


"""

##### with the help of matrix #####

mg = []

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    mg.append(temp)

for (u,v) in ipt:
    mg[u][v] = 1
    mg[v][u] = 1

for item in mg:
    print(item)
"""                
