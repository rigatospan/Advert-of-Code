file = 'd5_23.txt'
data = open(file).read().split('\n\n')

# seeds are in the first row
seeds = [int(s) for s in data[0].split()[1:] ]

# dictionary of the form node1: (node2, [(node2_start1, node1_star1, range1), (...)])
d = {}
for block in data[1:]:
    dat = block.splitlines()
    node_first, _, node_second = dat[0].split()[0].split('-')
    d[node_first] = (node_second, [tuple(map(int, line.split())) for line in dat[1:]])

start = 'seed'
stop = 'location'

def process_one_seed(seed_num):
    
    # define the current node and node number
    node, node_num = start, seed_num
    
    # go to the next node and corresponding next number until we reached the location
    while node != stop:
        
        # find next number in the next node
        next_node, ranges = d[node]
        
        # if node_num is not in the ranges it maps to itself
        next_node_num = node_num
        
        # find the correct range
        for (next_node_start, node_start, value) in ranges:
            if node_start <= node_num < node_start + value:
                next_node_num = next_node_start + node_num - node_start
                break
            
        # update the node to point to the next node  
        node, node_num = next_node, next_node_num
    
    return node_num

# find all the final locations of the seeds and print the lowest 
print(min([process_one_seed(seed) for seed in seeds]))