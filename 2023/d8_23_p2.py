from math import gcd

file = 'd8_23.txt'
data = open(file).read().splitlines()
# find the instuction string
instructions = data[0]
command_map = {'R': 1, 'L': 0}
# construct a dict of the form node: (node1, node2)
d = {}
for line in data[2:]:
    node, nodes = line.split('=')
    node = node.strip()
    node1, node2 = nodes.split(',')
    node1 = node1[2:]
    node2 = node2[1:-1]
    d[node] = (node1, node2)

# start at the node 'AAA', finish at the node 'ZZZ'
start_nodes = set(node for node in d if node[-1] == 'A')
stop_nodes = set(node for node in d if node[-1] == 'Z')

def process_one_node(start):
    i = 0
    node = start
    
    # find the first time that start reaches an end node; actually this is its period 
    while node not in stop_nodes:
        # if we reach the end start at the beginning of the string
        command = instructions[i % len(instructions)]
        # find the next node we go to
        number = command_map[command]
        node = d[node][number]
        
        i+=1
        
    return i

finished = []
for start in start_nodes:
    finished.append(process_one_node(start))

# find the smallest common multiple
p=1
for f in finished:
    p *= f//gcd(p, f)

print(f'all starting nodes will simultaneously end in ending node at iteration {p}')