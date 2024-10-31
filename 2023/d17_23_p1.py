import heapq
grid = [tuple(map(int,list(line))) for line in open('d17_23.txt').read().splitlines()]
a, b = len(grid), len(grid[0])

# steps in the four directions
directions = [(0,1), (0,-1), (1,0), (-1,0)]

# implement a min-priority queue; consider the same node with visited with a different direction a different node
# distance, row, col, (step_i, step_j), number_of_same_direction
# do not consider the source's distance 
pq = [(0, 0, 0, (0,0), 0)]

visited = set()

while pq:
    
    # pop the unvisited-node with the min-distance
    current_distance, i, j, direction, num_same_dir = heapq.heappop(pq)
    previous_stepi, previous_stepj = direction
    
    # if that node is already visited (by default at a smaller distance) 
    if (i, j, direction, num_same_dir) in visited:
        continue
    
    visited.add((i, j, direction, num_same_dir))
    
    # stop when we reached the exit
    if (i, j) == (a-1, b-1):
        print(f'final distance is {current_distance }')
        break
    
    # discover its adjacent nodes
    for stepi, stepj in directions:
        # do not consider going back 
        if (stepi, stepj) == (-previous_stepi, -previous_stepj):
            continue
        
        next_i, next_j = i+stepi, j+stepj
        if 0<=next_i< a and 0<=next_j < b:
            # check if is the same direction
            if (stepi, stepj) == (previous_stepi, previous_stepj):
                # if it is, push the next node into the heap only if it is less than 3 times the same direction
                if num_same_dir < 3:
                    heapq.heappush( pq, (current_distance+grid[next_i][next_j], next_i, next_j, (stepi,stepj), num_same_dir+1) )
            else:
                heapq.heappush( pq, (current_distance+grid[next_i][next_j], next_i, next_j, (stepi,stepj),1 ) )
                
# print(pq)