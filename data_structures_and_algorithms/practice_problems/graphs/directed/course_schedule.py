# 207. Course Schedule

# Cycle Detection
def course_schedule_i(n, courses):
    
    # need to build the graph
    # edge list -> adj list
    adj_list = [[] for i in range(n)]

    for src, dst in courses: # cool trick!
        adj_list[src].append(dst)

    visited = [-1]*n
    time = 0
    arr = [-1] * n # captured
    dep = [-1] * n
    for i in range(n):
        if visited[i] == -1:
            if not dfs(i, visited, adj_list, arr, dep, time):
                return False

    return True

def dfs(node, visited, adj_list, arr, dep, time):
    visited[node] = 1
    arr[node] = 1 # time+1
    for neighbor in adj_list[node]:
        if visited[neighbor] == -1: # tree edge
            # if first time being visited, it has never 
            # been in the call stack. so dep[neighbor] = -1
            return dfs(neighbor, visited, adj_list, arr, dep, time)
        else:
            # we've seen it before, potentially a cycle
            # back edge, is if we're looking at something still in the call stack
            if dep[neighbor] == -1: # cycle
                return False
            else:
                continue # cross edge/forward edge, doesn't matter. 
    dep[node] = 1 #time+1
    return True

r = course_schedule_i(2, [ [1,0] ])
print(r)

r = course_schedule_i(2, [ [1,0], [0,1] ])
print(r)

# -------------------------------------------------

def course_schedule_ii(n, courses):
    adj_list = [[] for i in range(n)]

    for src, dst in courses:
        adj_list[src].append(dst)

    visited = [-1]*n
    time = 0

    topsort = []

    arr = [-1] * n
    dep = [-1] * n
    for i in range(n):
        if visited[i] == -1:
            if not dfs(i, visited, adj_list, arr, dep, time, topsort):
                return []

    return topsort.reverse()

def dfs(node, visited, adj_list, arr, dep, time, topsort):
    visited[node] = 1
    arr[node] = time+1
    for neighbor in adj_list[node]:
        if visited[neighbor] == -1: # tree edge
            return dfs(neighbor, visited, adj_list, arr, dep, time, topsort)
        else:
            # we've seen it before, potentially a cycle
            # back edge, is if we're looking at something still in the call stack
            if dep[neighbor] == -1: # cycle
                return False
            else:
                continue # cross edge/forward edge, doesn't matter. 
    dep[node] = time+1
    # depart first, means we take it last
    topsort.append(node)

    return True