# 200 Number of Islands

from pprint import pprint

def num_islands(map):
    
    rows = len(map)
    cols = len(map[0])

    visited = [ [-1 for i in range(cols)] for j in range(rows) ]

    # copy of 2d matrix of visited

    # set of coordinates, or a copy of the map

    islands = 0
    for i in range(rows):
        for j in range(cols):

            if visited[i][j] == -1 and map[i][j] == 1:
                
                bfs(i,j, rows, cols, visited, map)
                islands += 1

    return islands

def bfs(i,j, rows, cols, visited, map):
    q = []
    q.append((i,j))

    visited[i][j]

    while q:
        curr_i, curr_j = q.pop(0)
        # get neighobrs
        neighbors = get_neighbors(curr_i, curr_j, rows, cols, map)
        for neighbor_i, neighbor_j in neighbors:
            if visited[neighbor_i][neighbor_j] == -1:
                q.append((neighbor_i, neighbor_j))
                visited[neighbor_i][neighbor_j] = 1
    return

def get_neighbors(i, j, rows, cols, map):
    # return a list of coordinates, which are valid neighbors of i,j

    neighbors = []

    # up 
    if i > 0 and map[i-1][j] == 1:
        neighbors.append((i-1, j)) 

    # left
    if j > 0 and map[i][j-1] == 1:
        neighbors.append((i, j-1))

    # down
    if i < rows-1 and map[i+1][j] == 1:
        neighbors.append((i+1, j))

    # right
    if j < cols-1 and map[i][j+1] == 1:
        neighbors.append((i, j+1))

    return neighbors

map = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

r = num_islands(map)
print(r)


map = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]

r = num_islands(map)
print(r)