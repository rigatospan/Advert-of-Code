def next_pt(pt: tuple, grid):
    '''Get the coord of the pt and its direction
    and return the next point with maybe 2 directions
    '''
    ax, ay = len(grid), len(grid[0])
    x, y, dx, dy = pt
    # next point
    nx, ny = x+dx, y+dy
    if not (0 <= nx < ax and 0 <= ny< ay ):
        return []
    
    symbol = grid[nx][ny]
    if symbol== '.':
        return [(nx, ny, dx, dy)]
    elif symbol=='|' and dy ==0:
        return [(nx, ny, dx, dy)]
    elif symbol=='|' and dy!=0:
        return [(nx, ny, 1, 0), (nx, ny, -1, 0)]
    elif symbol=='-' and dx ==0:
        return [(nx, ny, dx, dy)]
    elif symbol=='-' and dx!=0:
       return [(nx, ny, 0, 1), (nx, ny, 0, -1)]
    elif symbol=='\\':
        return [(nx, ny, dy, dx)]
    elif symbol=='/':
        return [(nx, ny, -dy, -dx)]


grid = [list(line) for line in open('d16_23.txt').read().splitlines()]

# light can enter from the left, right side, top or bottom side
initial_points1 = [(i, -1, 0,1) for i in range(len(grid))]
initial_points2 = [(i, len(grid[0]), 0,-1) for i in range(len(grid))]
initial_points3 = [(-1, j, 1,0) for j in range(len(grid[0]))]
initial_points4 = [(len(grid), j, -1, 0) for j in range(len(grid[0]))]
initial_points = initial_points1+initial_points2+initial_points3+initial_points4

max_so_far = 0
for pt in initial_points:
    visited_pts = set()
    unique_pts = set()
    current_points = [pt]

    while current_points:
        pt = current_points.pop()
        # print(f'current point is at {pt[0], pt[1]}')
        next_pts = next_pt(pt, grid)
        for pt in next_pts:
            if pt not in visited_pts:
                visited_pts.add(pt)
                unique_pts.add((pt[0], pt[1]))
                current_points.append(pt)
    
    if len(unique_pts)>max_so_far:
        max_so_far = len(unique_pts)

print(max_so_far)
