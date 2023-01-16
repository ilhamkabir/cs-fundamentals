

def kahns(n, edges):

    # 2 things, indegree array
    # when we decrement in degrees, also need a way to get the neighbors

    indegree = [0] * n
    adj_list = [[] for i in range(n)]

    for src, dst in edges:
        adj_list[src].append(dst)
        indegree[dst] += 1

    q = []

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topsort = []

    while q:
        curr = q.pop(0)
        topsort.append(curr)

        for neighbor in adj_list[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.push(neighbor)

    if len(topsort) != n:
        return []

    return topsort