def process_data(file):
    workflows, ratings = tuple(map(str.splitlines, open(file).read().split('\n\n')))
    ratings = [{eq[0]: eq[2:] for eq in rating[1:-1].split(',')} for rating in ratings]
    workflows = {w[:-1].split('{')[0]: [c.split(':') for c in w[:-1].split('{')[1].split(',')] for w in workflows}
    
    return ratings, workflows

def sum_a_leaf(state):
    '''return the product of the ranges of the intervals in the state
    '''
    values = [int(state[char][1])-int(state[char][0])+1 for char in state]
    p=1
    for v in values:
        p*=v
    return p
    
def return_intervals(low, high, value, operand):
    '''split the interval (low, high)into two intervals
    w.r.t the value and the operand
    '''
    if operand == '<' and value > low:
        if value < high:
            return (low, value-1) , (value, high)
        else:
            return (low, high) , None
    
    if operand == '>' and value < high:
        if value > low:
            return (value+1, high) , (low, value)
        else:
            return (low, high), None
    
    return None, None

def dfs(state_xmas, node, workflows):
    '''return the sum of the accepted leafs that are reached from the current node and state
    '''

    # check if we are at a leaf
    if node == 'A':
        return  sum_a_leaf(state_xmas)
    if node == 'R':
        return 0
    
    command = workflows[node]
    # sum the accepted values in the current node
    s = 0
    
    # store the values of the current state so that we reset it when we have finished with that node
    current_state = {char: values for char, values in state_xmas.items()}
    
    for condition in command:
        
        if len(condition) == 1:
            s+= dfs(state_xmas, condition[0], workflows) 
            continue
        
        # find the childrens of node and the new state that leads to them
        cond, next_node = condition
        char, operand, value = cond[0], cond[1], int(cond[2:])
        low, high = state_xmas[char]
        
        # new_interval is for the current examined child, while next_interval is the complementary interval
        # to update the state of the node for the next child
        new_interval, next_interval = return_intervals(low, high, value, operand)
        
        # if it is a valid interval go to the child
        if new_interval:
            
            # update the state for the child
            state_xmas[char] = new_interval
            s += dfs(state_xmas, next_node,  workflows)
        
            # after finishing with the child update the state of the node 
            if next_interval:
                state_xmas[char] =  next_interval
            # if there is no interval left stop the iteration through the childs of the node
            else:
                break
    
    # reset the state to that that entered the node after the dfs is finished for that node
    for char in state_xmas:
        state_xmas[char] = current_state[char]
    
    return s
        
file = 'd19_23.txt'
_ , workflows = process_data(file)
           
# at any node keep the state as a range of values that reach that node; values are inclusive
state_initially = {char:[1,4000] for char in 'xmas'}
node_in = 'in'
print(dfs(state_initially, node_in, workflows))