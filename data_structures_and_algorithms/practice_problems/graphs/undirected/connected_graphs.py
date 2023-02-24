
"""
    # 323: Number of Connected Components in an Undirected Graph
    
    Time/space complexity for BFS/DFS:

    space: n+m (adj_list) + n (visited) + 1 (components) + n (queue/call stack)
        O(n+m)

    time: m (build adj list) + (n+2m) (outerloop + traversal)
        O(n+m)
"""

def connected_components(n, edges, undirected=True):
    # build graph
    adj_list = [[] for i in range(n)]
    # DO NOT USE: adj_list = [[]]*n 

    # populate adj list
    for src, dst in edges:
        # print(src, dst)
        adj_list[src].append(dst)
        if undirected:
            adj_list[dst].append(src)

    # outer loop, multiple traversals 
    # how many traversals to visit all the nodes
    visited = [-1]*n # -1: not visited | 1: visited
    components = 0
    for i in range(n):
        if visited[i] == -1: # if not visited
            # run a traversal: bfs(i, components) or dfs(i, components)

            # bfs(i, visited, adj_list)
            dfs_recursive(i, visited, adj_list)
            # dfs_iterative(i, visited, adj_list)
            
            components += 1 # component only increments after entering an univisited node

    return components

def bfs(node, visited, adj_list):
    q = []
    q.append(node)
    visited[node] = 1
    while q:
        # get the univisted neighbors, add them to q, then visit them. 
        curr = q.pop(0)
        for neighbor in adj_list[curr]:
            if visited[neighbor] == -1:
                q.append(neighbor)
                visited[neighbor] = 1
    return

def dfs_recursive(node, visited, adj_list):
    visited[node] = 1
    for neighbor in adj_list[node]:
        if visited[neighbor] == -1:
            dfs_recursive(neighbor, visited, adj_list)
    return

def dfs_iterative(node, visited, adj_list):
    stack = []
    stack.append(node)
    visited[node] = 1
    while stack:
        # get the univisted neighbors, add them to q, then visit them. 
        curr = stack.pop()
        for neighbor in adj_list[curr]:
            if visited[neighbor] == -1:
                stack.append(neighbor)
                visited[neighbor] = 1
    return


edges = [ [0,1], [1,2], [3,4] ]
r = connected_components(5, edges)
print('Conn comps for edges', edges, ':', r)

edges = [ [0,1], [1,2], [2,3], [3,4] ]
r = connected_components(5, edges)
print('Conn comps for edges', edges, ':', r)

