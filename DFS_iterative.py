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
#resursive
def dfs(visited,graph,node):

    if node not in visited:
        visited.add(node)
        print('Visited ',node)
        
        for neighbor_nodes in graph[node]:

            dfs(visited,graph,neighbor_nodes)


dfs(visited, graph, 'A')



#iterative
visited =set()
stack = ['A']

while(stack):

    new_node = stack.pop()
    
    if new_node not in visited:
        visited.add(new_node)
        print('Visited ',new_node)
        
        for neighbor_nodes in graph[new_node]:

            stack.append(neighbor_nodes)

