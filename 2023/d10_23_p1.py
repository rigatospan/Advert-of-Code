file = 'd10_23.txt'
grid = [list(line) for line in open(file).read().splitlines()]
a, b = len(grid), len(grid[0])

# defines the possible nbrs of each symbol
char_to_nbrs = {'F': [(0,1), (1,0)] ,'-': [(0,1),(0,-1)], '7':[(0,-1),(1,0)], 
        '|':[(-1,0),(1,0)],  'J': [(0,-1),(-1,0)] , 'L': [(-1,0),(0,1)], 
        '.': [(0,0)]}
steps  = ((-1, 0), (1, 0), (0, -1), (0, 1))

# find position of S 
for i, line in enumerate(grid):
    if 'S' in line:
        start_i, start_j = i, line.index('S')
        break
path = [(start_i, start_j)]

# find where 'S' leads next
# go to the nbrs of 'S' and find if one the two that leads back to 'S'
for ni, nj in steps:
    if 0 <= start_i+ni < a and 0<= start_j+nj < b:
        # check if the nbrs leads back to 'S'
        for di, dj in char_to_nbrs[grid[start_i+ni][start_j+nj]]:
            if (ni+di, nj+dj) == (0, 0):
                path.append((start_i+ni, start_j+nj))

# remove one of the two nbrs of S
path.pop()

# loop until we find S again
while path[0] != path[-1]:
    second_last_node_i, second_last_node_j = path[-2]
    last_node_i, last_node_j = path[-1]
    
    # find the next node and add it to path
    for di, dj in char_to_nbrs[grid[last_node_i][last_node_j]]:
        
        # find the next node, not the previous
        if (last_node_i+di, last_node_j+dj) != (second_last_node_i, second_last_node_j):
            path.append((last_node_i+di, last_node_j+dj))

print(f'furthest away point from S takes {(len(path)-1)//2} steps to reach')