file = 'd21_23.txt'
grid = [list(line) for line in open(file).read().splitlines()]
a, b = len(grid), len(grid[0])

# find where is 'S'
for i, line in enumerate(grid):
    if 'S' in line:
        start_i, start_j = i, line.index('S')
        break 

# step we can take 
steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

# maintain a list of the points seen for first time; (i, j)
points = [(start_i, start_j)]
# maintain a list of points already seen and at the iteration % 2 that they 
# where first discovered (i, j, n_iteration % 2)
seen_points = set()

def process_one_point(i, j, n_iter):
    '''given a point (i, j) and the number of iteration n_inter
    return the list of points that can be reached by (i, j) 
    and have not already be seen
    '''
    
    next_points_from_one_point = []
    for di, dj in steps:
        if 0 <= i+di < a and 0 <= j+dj < b:
            if grid[i+di][j+dj] != '#'  and (i+di, j+dj, n_iter % 2) not in seen_points:
                next_points_from_one_point.append((i+di, j+dj))
                seen_points.add((i+di, j+dj, n_iter % 2))
    
    return next_points_from_one_point

number_iterations = 64             
for i in range(1, number_iterations+1):
    next_points = []
    
    # iterate through all current points and look for next points
    while points:
        pti, ptj = points.pop()
        next_points.extend(process_one_point(pti, ptj, i))
    
    # update the points to the next points
    points = next_points

print(sum([1 for (i, j, n) in seen_points if n==number_iterations%2]))

################################################################
################################################################

# solution 2; 
# maintain a dict of the points seen for first time and the previous points that lead to that point
# {(i, j): [(i1, j1, i2, j2)])
points = {(start_i, start_j): []}

n_even, n_odd = 1, 0
number_iterations = 64            

for i in range(1, number_iterations+1):
    next_points = {}
    
    # iterate through all current points and look for next points not seen before
    for (pti, ptj) in points:
        
        for di, dj in steps:
            next_i, next_j = pti+di, ptj+dj
            if 0 <= next_i < a and 0 <= next_j < b:
                # check if the next point is in the points that lead to it
                if grid[next_i][next_j] != '#' and (next_i, next_j) not in points[(pti, ptj)]:
                    # add it 
                    if (next_i, next_j) in next_points:
                        next_points[(next_i, next_j)].append((pti, ptj))
                    else: 
                        next_points[(next_i, next_j)] = [(pti, ptj)]
    
    # add the new points
    if i%2 == 0:
        n_even += len(next_points)
    else:
        n_odd += len(next_points)
        
    # update the points to the next points
    points = next_points

print(f'number of points reached after {number_iterations} is {n_even if number_iterations%2==0 else n_odd}')