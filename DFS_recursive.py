# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


visited =set()

def dfs(visited,graph,node):

    if node not in visited:
        visited.add(node)
        print('Visited ',node)
        
        for neighbor_nodes in graph[node]:

            dfs(visited,graph,neighbor_nodes)



dfs(visited, graph, 'A')