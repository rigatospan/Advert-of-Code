file = 'd5_23.txt'
data = open(file).read().split('\n\n')

# seeds are in the first row, now in pairs
seeds = [(int(start), int(start)+int(value)-1) for start, value in zip(data[0].split()[1::2], data[0].split()[2::2]) ]

# dictionary of the form node1: (node2, [(node2_start1, node1_start1, range1), (...)])
d = {}
for block in data[1:]:
    dat = block.splitlines()
    node_first, _, node_second = dat[0].split()[0].split('-')
    # sort in ascending order of the node1_start
    d[node_first] = (node_second, sorted(list(tuple(map(int, line.split())) for line in dat[1:]), key= lambda values: values[1]) )

start = 'seed'
stop = 'location'

def process_seed_interval(seed_intervals):
    
    # define the current node and node number
    node = start
    node_intervals = seed_intervals
    
    # go to the next node and corresponding next number until we reached the location
    while node != stop:
        
        # find next node in the next node
        next_node, ranges = d[node]
        
        # map all the intervals to the next node
        next_node_intervals = []
        
        while node_intervals:
        
            a, b = node_intervals.pop()
            
            # find the intersection of the interval with some interval in next_node ranges
            for (next_node_start, node_start, value) in ranges:
                
                # find intersection between [a, b] and [node_start, node_start+value-1]
                inter_min, inter_max = max(a, node_start), min(b, node_start+value-1)
                
                # check if it a valid interval
                if inter_min<=inter_max:
                    # find the mapped values for the next_interval
                    next_a = next_node_start + inter_min - node_start
                    next_b = next_node_start + inter_max - node_start 
                    next_node_intervals.append((next_a, next_b) )
                
                    # find also the complement of the intersection and add it to the node_intervals
                    # to be examined for other intersection with ranges
                    if a < inter_min and b >= node_start:
                        node_intervals.append((a, node_start-1))
                    if b > inter_max and a >= node_start:
                        node_intervals.append((inter_max+1, b))
                    break
            else:
                # if there is no intersection with any of the next_node ranges intervals
                # [a, b] should be added as it is on the next_node_intervals
                next_node_intervals.append((a, b))
         
        # update the node to point to the next node and the intervals  
        node, node_intervals = next_node, next_node_intervals
    
    return node_intervals

# find the min value at the location intervals
print(min(process_seed_interval(seeds))[0])