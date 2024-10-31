def get_vertices(directions: list[str]):
    current_vertex = (0,0)
    points = [current_vertex]
    moves = {'R': (0,1), 'L': (0,-1), 'D': (1,0), 'U': (-1,0)}
    for direction, step in directions:
        move_x, move_y = moves[direction]
        next_vertex = (current_vertex[0]+move_x*int(step), current_vertex[1]+move_y*int(step))
        points.append(next_vertex)
        current_vertex = next_vertex
    points.pop()
    return points

def get_area(points):
    
    return abs(sum([points[i][0]*points[i+1][1]-points[i+1][0]*points[i][1] for i in range(-1,len(points)-1)]))//2

def get_boundary_points(points):
    perimeter = sum( [abs(points[i][0]-points[i+1][0])+abs(points[i][1]-points[i+1][1]) for i in range(-1, len(points)-1)] )
    
    return perimeter
        
directions = [line.split()[-1][1:-1] for line in open('d18_23.txt').read().splitlines()]
num_to_dir = {0:'R', 1:'D', 2:'L', 3:'U'}

# transform the hexadecimal string into decimal form
directions = [( num_to_dir[int(d[-1])], int(d[1:-1], base=16)) for d in directions]

# print(directions)
points = get_vertices(directions)
area = get_area(points)
boundary_points = get_boundary_points(points)
# pick's theorem: area = interior_points + boundary_points/2 -1
print(f'area is {area}, number of boundary points is {boundary_points}, total points is {area+boundary_points//2+1}')