def is_bipartite(n, edges, undirected=True):
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
    group = [-1]*n # subsets # 0 or 1

    for i in range(n):
        if visited[i] == -1: # if not visited
            group[i] = 0
            if not dfs(i, visited, group, adj_list):
                return False

    return True

# _is_bipartite = True
def dfs(node, visited, group, adj_list):
    visited[node] = 1
    for neighbor in adj_list[node]:
        if visited[neighbor] == -1:
            # tree edge, seeing for first time
            group[neighbor] = 1-group[node] # 1-0=1 | 1-1=0
            return dfs(neighbor, visited, group, adj_list) # return to bubble up
            # _is_bipartite = _is_bipartite and dfs(neighbor, visited, group, adj_list)
        else:
            # seeing something i've seen before + we're the same color => bad!
            if group[neighbor] == group[node]:
                return False
                # _is_bipartite = False
    return True
    # return _is_bipartite


edges = [ [0,1], [0,2], [0,3], [1,4] ]
r = is_bipartite(5, edges)
print('is bipartite', edges, ':', r)

edges = [ [0,1], [1,2], [2,3], [1,3], [1,4] ]
r = is_bipartite(5, edges)
print('is bipartite', edges, ':', r)

# ----------------------------------------------

# 886. Possible Bipartition

def possible_bipartition(n, dislikes):
    pass


dislikes = [ [1,2], [1,3], [2,4] ]
r = possible_bipartition(4, dislikes)
print('dislikes: ', dislikes, '| possible bipartition:', r)

dislikes = [ [1,2], [1,3], [2,3] ]
r = possible_bipartition(3, dislikes)
print('dislikes: ', dislikes, '| possible bipartition:', r)

dislikes = [ [1,2], [2,3], [3,4], [4,5], [1,5] ]
r = possible_bipartition(5, dislikes)
print('dislikes: ', dislikes, '| possible bipartition:', r)