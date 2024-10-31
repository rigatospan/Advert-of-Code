from collections import deque
import copy

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

def push_botton_once(modules, debug = True):
    global high_pulses, low_pulses
    
    # start by sending a 0 to the broadcaster and to all its nodes
    q = deque([(node, 'broadcaster', 0) for node in modules['broadcaster'][2]])

    low_pulses+=len(q)

    # iterate while there are nodes with a signal
    while q:
        # consider the first node and signal
        node, node_sender, signal = q.popleft()

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
                if send_signal==1:
                    high_pulses+=1
                else:
                    low_pulses+=1


        if modules[node][0] == '&':
            # update the value for that node sender
            modules[node][1][node_sender] = signal

            # send a pulse 0 if all state is 1 else send 1
            send_signal = 0 if all([s==1 for s in modules[node][1].values()]) else 1
            for nbr in modules[node][2]:
                q.append((nbr, node, send_signal))
                if send_signal:
                    high_pulses+=1
                else:
                    low_pulses+=1

modules = process_data('d20_23.txt')

original_state = copy.deepcopy(modules)

# times to push the button
n = 1001
low_pulses = 0
high_pulses = 0
for i in range(1, n):

    # push the botton send a low pulse to broadcaster
    low_pulses+=1
    push_botton_once(modules, debug=False)
    if original_state == modules:
        print(f'found a cycle after {i+1} iterations')
        break 

cycle = i

print(f'low pulses for one cycle are {low_pulses}, high pulses are {high_pulses}')
print(f'low pulses are {low_pulses*1000/cycle}, high pulses are {high_pulses*1000/cycle}, product {low_pulses*1000/cycle*high_pulses*1000/cycle}')