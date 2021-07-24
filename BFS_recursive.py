from collections import deque
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set() # List to keep track of visited nodes.
queue = deque('A')     #Initialize a queue


def bfs(visited,graph,queue):

    if not q:
        return
    
    else:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            print('Visited ',node)
        
        for neighbor_nodes in graph[node]:

            dfs(visited,graph,neighbor_nodes)



dfs(visited, graph, 'A')