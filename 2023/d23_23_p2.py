file = 'd23_23.txt'
grid = [list(line) for line in open(file).read().splitlines()]
a, b = len(grid), len(grid[0])
start = (0, grid[0].index('.'))
stop = (a-1, grid[a-1].index('.'))
moves = ((1,0), (-1,0), (0,1), (0,-1))
split = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

# set the split symbols into normal '.'
for i in range(a):
    for j in range(b):
        if grid[i][j] in split:
            grid[i][j] = '.'

# find the neighbourhs
vertices = tuple((i,j) for i in range(a) for j in range(b) if grid[i][j] != '#')
nbrs = {v:[] for v in vertices}

for i,j in vertices:
    symbol = grid[i][j]
    if symbol in split:
        pos_moves = [split[symbol]]
    else:
        pos_moves = moves
        
    for di, dj in pos_moves:
        if 0<=i+di<a and 0 <= j+dj <a: 
            if grid[i+di][j+dj] == '.':
                nbrs[(i, j)].append((i+di, j+dj))
            elif grid[i+di][j+dj] in split:
                if (di, dj) == split[grid[i+di][j+dj]]:
                    nbrs[(i, j)].append((i+di, j+dj))

# construct a graph with vertices the grid-points that have at least 3 nbrs and the start point
# edges two nbrs vertices and weights the distance of that edge 
# find points that have at least 3 nbrs and consider those as the vertice
vertices_graph = set()
vertices_graph.add(start)

for i in range(a):
    for j in range(b):
        symbol = grid[i][j]
        if symbol != '.':
            continue
        # find number of nbrs
        num_nbrs = 0
        for di, dj in moves:
            if 0 <= i+di < a and 0 <= j+dj < a and grid[i+di][j+dj] != '#': 
                num_nbrs+=1
        
        if num_nbrs >=3:
            vertices_graph.add((i, j))

def dfs(node, visited, nbrs, vertices_graph, w):
    if node in vertices_graph or node == stop:
        return node, w
    
    visited[node] = True
    
    for nhbr_node in nbrs[node]:
        if not visited[nhbr_node]:
            return dfs(nhbr_node, visited, nbrs, vertices_graph, w+1)

nbrs_graph = {v:[] for v in vertices_graph}
for v in vertices_graph:
    for v_nbr in nbrs[v]:
        visited = {n: False for n in vertices}
        visited[v] = True
        u, w = dfs(v_nbr, visited, nbrs, vertices_graph, 1)
        nbrs_graph[v].append((u, w))

visited_graph = {v: False for v in vertices}

def dfs_graph(node, stop, vertices_graph, nbrs_graph, visited_graph):
    if node == stop:
        return 0
    
    visited_graph[node] = True
    max_distance = float('-inf')
    
    for nhbr_node,w in nbrs_graph[node]:
        if not visited_graph[nhbr_node]:
            max_distance = max(max_distance, w+dfs_graph(nhbr_node, stop, vertices_graph, nbrs_graph, visited_graph) )
    
    visited_graph[node] = False
    
    return max_distance

# runs in 30 sec
print(dfs_graph(start, stop, vertices_graph, nbrs_graph, visited_graph))