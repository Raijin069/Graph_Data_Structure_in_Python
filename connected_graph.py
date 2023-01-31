# edges = [['A','B'],['A','C'],['A','D'],['D','E'],['B','E']]
# nodes = ['A','B','C','D','E']
edges = [['A','B'],['A','C'],['A','D'],['D','E'],
        ['B','E'],['F','H'],['F','G'],['I','J']]
nodes = ['A','B','C','D','E','F','G','H','I','J','K']

# def dfs(graph,node,visited = set()):
#     print(node)
#     visited.add(node)
#     for child in graph[node]:
#         if child not in visited:
#             dfs(graph,child,visited) 


# def no_of_node(graph,node,visited = set()):
#     # print(node)
#     visited.add(node)
#     sm = 0
#     for child in graph[node]:
#         if child not in visited:
#             sm += no_of_node(graph,child,visited) 
#     return sm+1

def dfs(graph,node,visited = set()):
    print(node)
    visited.add(node)
    sm = 0
    for child in graph[node]:
        if child not in visited:
            sm += dfs(graph,child,visited) 
    return sm+1

graph = {}
for i in nodes:
    graph[i] = []

for (u,v) in edges:
    graph[u].append(v)     
    graph[v].append(u)

for i in graph.items():
    print(i) 

# dfs(graph,'A')        
# print(no_of_node(graph,'A'))
answer = []
visited = set()
for item in nodes:
    if item not in visited:
        temp = dfs(graph,item,visited)
        answer.append(temp)

print(answer)