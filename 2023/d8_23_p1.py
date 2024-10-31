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
start = 'AAA'
stop = 'ZZZ'

i = 0
node = start
while node!= stop:
    # if we reach the end start at the beginning of the string
    command = instructions[i % len(instructions)]
    # find the next node we go to
    number = command_map[command]
    node = d[node][number]
    
    i+=1

print(f'find node "ZZZ" at iteration {i}')