# 909. Snakes and Ladders

# cross edges won't always be back edges 
# (only except is if you're on the end of a ladder)

# BFS
def snakes_ladderes(n, s_l):

    goal = n

    visited = [-1]*(n+1) # distance so far. what is the dist from 0 to node i
    # parent = [-1]*n

    q = []
    q.append(0)
    visited[0] = 0

    while q:
        curr = q.pop(0)

        for neighbor in range(curr+1, min(curr+7, goal+1)): # 7 b/c upper bound is exclusive (n-1)). don't want to go past goal.
            # get unvisted neighbors, add them to the q and visit them.
            landed = s_l[neighbor]
            if visited[landed] == -1:
                q.append(landed)
                # 1 dice away from current spot
                visited[landed] = visited[curr] + 1 # prev dist + 1
        
            if landed == goal:
                shortest_distance = visited[landed]
                #  while landed != 0:
                #      print(landed)
                #      landed = parent[landed]

                # first time found will be the shortest path
                # so we never need to find the min
                return shortest_distance 

    return -1 # not possible (not connected)

s_l = [ 
    0, 1, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
    35, 15, 16, 13, 18, 29, 20, 21, 22, 23, 24, 25, 
    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
]

r = snakes_ladderes(36, s_l)
print(r)
