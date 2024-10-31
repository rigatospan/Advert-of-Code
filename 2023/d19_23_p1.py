def process_data(file):
    workflows, ratings = tuple(map(str.splitlines, open(file).read().split('\n\n')))
    ratings = [{eq[0]: eq[2:] for eq in rating[1:-1].split(',')} for rating in ratings]
    workflows = {w[:-1].split('{')[0]: [c.split(':') for c in w[:-1].split('{')[1].split(',')] for w in workflows}
    
    return ratings, workflows

def process_one_command(rating, command):
    ''' take a rating of the form 
    {'x': '787', 'm': '2655', 'a': '1222', 's': '2876'}
    and a command of the form 
    [['a<2006', 'qkq'], ['m>2090', 'A'], ['rfg']]
    and return either accepted 'A', rejected 'R' or the next node 'xxx'
    '''

    for condition in command:
        if len(condition) == 1:
            return condition[0]
        
        cond, result = condition
        # unpack the character if the condition
        character, operant_value = cond[0], cond[1:]
        # check if the condition is met by the value of that character in rating
        if eval(rating[character]+operant_value):
            return result
        
def process_one_rating(workflows, rating, start):
    '''process the rating in all workflows
    start
    '''
    command = workflows[start]
    result = process_one_command(rating, command)
    if result in 'AR':
        return result
    
    return process_one_rating(workflows, rating, result)

def process_all_ratings(workflows, ratings):
    '''
    return a list of either 'A' or 'R' for all ratings
    '''

    return [process_one_rating(workflows, rating, start='in') for rating in ratings]

def find_sum_of_accepted(ratings, results):
    '''return the sum of the values in the ratings of those that are accepted
    '''
    return sum([sum(list(map(int, ratings[i].values())) ) for i,r in enumerate(results) if r=='A'])

file = 'd19_23.txt'
ratings, workflows = process_data(file)
results = process_all_ratings(workflows, ratings)
print(f'sum of the values of accepted ratings is {find_sum_of_accepted(ratings, results)}' )