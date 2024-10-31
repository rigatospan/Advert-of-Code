from collections import deque
from math import gcd

def process_data(file:str):

    modules = {}
    for line in open(file).read().splitlines():
        modul , outps = line.split('->')
        modul = modul.strip()
        nbhrs = [n.strip() for n in outps.split(',')]
        if modul[0] == '&':
            node = modul[1:]
            type = '&'
            state = {}
        elif modul[0] == '%':
            node = modul[1:]
            type = '%'
            state = 0
        else:
            node = modul
            type = modul
            state = None
        
        modules[node] = [type, state, nbhrs]
    
    not_in_modules = []
    for node in modules:
        type, state, nbhrs = modules[node]
        for nbr in nbhrs:
            # check if there is a nbr which is not on the modules, i.e does not have output connections
            if nbr not in modules:
                not_in_modules.append(nbr)
                continue

            if modules[nbr][0] == '&':
                modules[nbr][1][node] = 0
    
    for no_output_node in not_in_modules:
        modules[no_output_node] = [None, None, []]

    return modules

def push_botton_once(modules, nodes_to_source, i, nodes_to_source_outputs_one, debug = True):
    
    # start by sending a 0 to the broadcaster and to all its nodes
    q = deque([(node, 'broadcaster', 0) for node in modules['broadcaster'][2]])

    # iterate while there are nodes with a signal
    while q:

        # consider the first node and signal
        node, node_sender, signal = q.popleft()

        # check if a node_to_source node outputs 1 to the source for the first time
        if node_sender in nodes_to_source and signal == 1 and nodes_to_source_outputs_one[node_sender] == None:
            if debug:
                print(f'node {node_sender} send 1 at iteration {i}')
            nodes_to_source_outputs_one[node_sender] = i
 
        if debug:
            print(f'{node_sender} send a {signal} pulse to {node}')

        if modules[node][0] == '%':
            # if the signal is 1 nothing happens
            if signal:
                continue

            # if the signal is 0 the it flips its state
            modules[node][1] = (modules[node][1]+1) % 2

            # then send to its nbhrs a signal with value of the state (i.e. 1 or 0)
            send_signal = modules[node][1]
            for nbr in modules[node][2]:
                q.append((nbr, node, send_signal)) 

        if modules[node][0] == '&':
            # update the value for that node sender
            modules[node][1][node_sender] = signal

            # send a pulse 0 if all state is 1 else send 1
            send_signal = 0 if all([s==1 for s in modules[node][1].values()]) else 1
            for nbr in modules[node][2]:
                q.append((nbr, node, send_signal))

modules = process_data('d20_23.txt')

# find the source node that leads to node 'rx'
for node in modules:
    if 'rx' in modules[node][2]:
        source_to_rx = node

# find the nodes that lead to the source 
nodes_to_source = {}
for node in modules:
    if source_to_rx in modules[node][2]:
        nodes_to_source[node] = 0

# source will outpur 0 when all the nodes_to_source nodes output 1 all at the same time
# find for each individually when it outpurs 1
# then find the smaller common multiple

nodes_to_source_outputs_one = {node: None for node in nodes_to_source}

# push the button until all the nodes_to_source nodes output one at some iteration
i=1
while None in nodes_to_source_outputs_one.values():
    
    # push the botton send a low pulse to broadcaster
    push_botton_once(modules, nodes_to_source, i, nodes_to_source_outputs_one, debug=False)
    i+=1

print(f'nodes leading to source each outputs 1 at iteration {nodes_to_source_outputs_one}')

# find the smaller common multiple of those values
product = 1
for p in nodes_to_source_outputs_one.values():
    product *= p // gcd(p, product)

print(f'circuit will output 0 at iteration {int(product)}')