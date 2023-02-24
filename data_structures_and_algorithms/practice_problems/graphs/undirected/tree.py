# 261 Graph Valid Tree

def is_tree(n, edges, undirected=True):
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
    parent = [-1]*n # to ignore tree edge in reverse when counting cross edges
    components = 0
    for i in range(n):
        if visited[i] == -1: # if not visited

            if components == 1:
                # about to increment
                return False

            # run a traversal: bfs(i, components) or dfs(i, components)

            # if not bfs(i, visited, parent, adj_list): return False
            # if not dfs_recursive(i, visited, parent, adj_list): return False
            # if not dfs_iterative(i, visited, parent, adj_list): return False
            
            components += 1 # component only incrments after entering an univisited node

    return True

def bfs(node, visited, parent, adj_list):
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
                parent[neighbor] = curr # parent of neighbor is current
            else:
                # could be a corss edge... NOT GUARANTEED! (tree edge in reverse)
                # check by keeping a parent array
                if parent[curr] == neighbor: # reverse 
                    # tree edge in reverse
                    continue
                else:
                    # cross edge found
                    return False
    return True

def dfs_recursive(node, visited, parent, adj_list):
    visited[node] = 1
    for neighbor in adj_list[node]:
        if visited[neighbor] == -1:
            parent[neighbor] == node
            return dfs_recursive(neighbor, visited, parent, adj_list) # return to bubble result back up
        else:
            # check if back edge in reverse
            if parent[node] == neighbor:
                continue
            else:
                # back edge
                return False
    return True

def dfs_iterative(node, visited, parent, adj_list):
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
                parent[neighbor] = curr # parent of neighbor is current
            else:
                # could be a corss edge... NOT GUARANTEED! (back edge in reverse)
                # check by keeping a parent array
                if parent[curr] == neighbor: # reverse 
                    # back edge in reverse
                    continue
                else:
                    # cross edge found
                    return False
    return True



edges = [ [0,1], [0,2], [0,3], [1,4] ]
r = is_tree(5, edges)
print('is tree', edges, ':', r)

edges = [ [0,1], [1,2], [2,3], [1,3], [1,4] ]
r = is_tree(5, edges)
print('is tree', edges, ':', r)