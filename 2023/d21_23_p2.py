file = 'd21_23_ex.txt'
grid = [list(line) for line in open(file).read().splitlines()]
a, b = len(grid), len(grid[0])

# find where is 'S'
for i, line in enumerate(grid):
    if 'S' in line:
        start_i, start_j = i, line.index('S')
        break 

# step we can take 
steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

# number the current grid as the grid (0, 0)
# number subsequent discovered grid in all 4 directions by coordinates (x, y)

# maintain a list of the points seen for first time; (i, j, x, y)
points = [(start_i, start_j, 0, 0)]
# maintain a list of points already seen and at the iteration % 2 that they 
# where first discovered (i, j, n_iteration % 2, x, y)
seen_points = set()

def process_one_point(i, j, n_iter, x, y):
    '''given a point (i, j), the number of iteration n_inter
    and the coordinates of the points grid (x, y)
    return the list of points that can be reached by (i, j) 
    and have not already be seen
    '''
    
    next_points_from_one_point = []
    for di, dj in steps:
        
        # find the next coordinates and grid coordinates of the nbhr point
        next_i, next_j = i+di, j+dj
        next_x, next_y = x, y
        
        if next_i == -1:
            next_x = x-1
        elif next_i == a:
            next_x = x+1
        elif next_j == -1:
            next_y = y-1
        elif next_j == b:
            next_y = y+1
        
        next_i %= a
        next_j %= b
        
        if grid[next_i][next_j] != '#'  and (next_i, next_j, n_iter % 2, next_x, next_y) not in seen_points:
            next_points_from_one_point.append((next_i, next_j, next_x, next_y))
            seen_points.add((next_i, next_j, n_iter % 2, next_x, next_y))
    
    return next_points_from_one_point

number_iterations = 5000
for i in range(1, number_iterations+1):
    next_points = []
    
    # iterate through all current points and look for next points
    while points:
        pti, ptj, x, y = points.pop()
        next_points.extend(process_one_point(pti, ptj, i, x, y))
    
    # update the points to the next points
    points = next_points
    if i%500 == 0:
        print(f'number of seen points at {i} are {len(seen_points)}')
        print(f'number of next_points is {len(next_points)}')

print(sum([1 for (i, j, n, x, y) in seen_points if n==number_iterations%2]))