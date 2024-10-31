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

pt = (0, -1, 0, 1)
visited_pts = set()
unique_pts = set()
current_points = [(0, -1, 0, 1)]

while current_points:
    pt = current_points.pop()
    # print(f'current point is at {pt[0], pt[1]}')
    next_pts = next_pt(pt, grid)
    for pt in next_pts:
        if pt not in visited_pts:
            visited_pts.add(pt)
            unique_pts.add((pt[0], pt[1]))
            current_points.append(pt)

print(len(visited_pts), len(unique_pts))
